# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

# routes/runner.py

import logging
import uuid

from fastapi import (
    APIRouter,
    Request,
    status
)
from starlette.responses import JSONResponse

from backend.app.app_def import (
    API_VERSION,
    DB_COLLECTION_ACTIVITY,
    DB_NAME_ACTIVITY,
    CACHE_KEY_ACTIVITY
)
from backend.app.cache import (
    cache_get,
    cache_set,
    cache_invalidate
)
from backend.models.activity import (
    Activity,
    ActivityCreate,
    ActivityUpdate
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(f"/api/{API_VERSION}/activities",
            tags=["activity"],
            response_model=list[Activity],
            status_code=status.HTTP_200_OK)
async def get_all_activities(request: Request):
    """ Get the status of all runners. """

    cached = cache_get(CACHE_KEY_ACTIVITY)
    if cached is not None:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=cached)

    db = request.app.state.mdb

    # Retrieve all activity from database
    activities = await db.find(DB_NAME_ACTIVITY,
                               DB_COLLECTION_ACTIVITY.name,
                               {})

    # Update cache
    cache_set(CACHE_KEY_ACTIVITY, activities)

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=activities)


@router.post(f"/api/{API_VERSION}/activities",
             tags=["activity"],
             response_model=Activity,
             status_code=status.HTTP_201_CREATED)
async def create_activity(request: Request,
                          activity: ActivityCreate):
    """Endpoint to create activity"""

    db = request.app.state.mdb

    # Prepare request data
    request_data = activity.model_dump()

    # Check no duplicated title
    existing = await db.find_one(DB_NAME_ACTIVITY, DB_COLLECTION_ACTIVITY.name, {
        "title": request_data["title"],
    })
    if existing is not None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": f"title {request_data["title"]} already exists"}
        )

    # Assign _id
    db_insert = Activity(**request_data).model_dump()
    db_insert["_id"] = str(uuid.uuid4())

    # Create the activity in the database
    await db.create(DB_NAME_ACTIVITY,
                    DB_COLLECTION_ACTIVITY.name,
                    db_insert)

    # Invalidate cache so next GET is new activity
    cache_invalidate(CACHE_KEY_ACTIVITY)

    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=request_data)


@router.put(f"/api/{API_VERSION}/activities/{{activity_id}}",
            tags=["activity"],
            response_model=Activity,
            status_code=status.HTTP_200_OK)
async def update_activity(request: Request,
                          activity: ActivityUpdate):
    """Endpoint to update activity"""


@router.delete(f"/api/{API_VERSION}/activities/{{activity_id}}",
               tags=["activity"],
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_activity(request: Request,
                          activity_id: str):
    """Endpoint to delete activity"""
