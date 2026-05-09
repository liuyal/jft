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

from backend.app.app_def import (
    API_VERSION,
    DB_COLLECTION_ACTIVITY,
    DB_NAME_ACTIVITY
)
from backend.app.cache import (
    cache_get,
    cache_set
)
from backend.models.activity import Activity

router = APIRouter()

logger = logging.getLogger(__name__)

DB_COLLECTION_ACTIVITY = DB_COLLECTION_ACTIVITY.name

@router.get(f"/api/{API_VERSION}/activities",
            tags=["activity"],
            response_model=list[Activity],
            status_code=status.HTTP_200_OK)
async def get_all_activities(request: Request):
    """ Get the status of all runners. """

    cache_key = "activities:all"
    cached = cache_get(cache_key)
    if cached is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=cached)

    db = request.app.state.mdb

    # Retrieve all projects from database
    activities = await db.find(DB_NAME_ACTIVITY, DB_COLLECTION_ACTIVITY, {})

    cache_set(cache_key, activities)
    return JSONResponse(status_code=status.HTTP_200_OK, content=activities)
