# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

# model/tracker.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Activity(BaseModel):
    _id: str
    activity_type: str
    title: str
    date: str
    distance: float
    elevation_gain: float | None
    start_time: int | None
    end_time: int | None
    duration: float | None
    model_config = {"extra": "forbid"}


class ActivityCreate(BaseModel):
    activity_type: str
    title: str
    date: str
    distance: float
    elevation_gain: float | None = None
    start_time: int | None = None
    end_time: int | None = None
    duration: float | None = None
    model_config = {"extra": "forbid"}


class ActivityUpdate(BaseModel):
    activity_type: str | None = None
    title: str | None = None
    date: str | None = None
    distance: float | None = None
    elevation_gain: float | None = None
    start_time: int | None = None
    end_time: int | None = None
    duration: float | None = None
    model_config = {"extra": "forbid"}
