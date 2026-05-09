# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

# routes/runner.py

import logging

from fastapi import (
    APIRouter,
    Request,
    status
)
from starlette.responses import JSONResponse

from backend.app.app_def import API_VERSION
from backend.models.activity import Activity

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(f"/api/{API_VERSION}/activies",
            tags=["activity"],
            response_model=Activity,
            status_code=status.HTTP_200_OK)
async def get_runners_status(request: Request):
    """ Get the status of all runners. """

    return JSONResponse(status_code=status.HTTP_200_OK)
