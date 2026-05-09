# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

# app/correlation.py
#
# Provides per-request correlation IDs that propagate automatically through
# every log line emitted during an async request, regardless of call depth.

import logging
import uuid
from contextvars import ContextVar

_FALLBACK = "-"
_request_id_var: ContextVar[str] = ContextVar("request_id", default=_FALLBACK)


def get_request_id() -> str:
    """Return the request ID for the currently running async task."""

    return _request_id_var.get()


def set_request_id(request_id: str | None = None) -> str:
    """Set (or generate) the request ID for the current async task.

    Returns the ID that was set so the caller can echo it in response headers.
    """

    rid = request_id or str(uuid.uuid4())
    _request_id_var.set(rid)
    return rid


class CorrelationFilter(logging.Filter):
    """Injects ``request_id`` into every LogRecord.

    Reads from the ContextVar so the value is always correct for the
    currently executing async task, even under high concurrency.

    Registered in log_conf.yaml via dictConfig's () factory syntax so it is
    active before the first log record is emitted — no startup race condition.
    """

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = get_request_id()
        return True
