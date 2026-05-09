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
    activity_key: str
    activity_type: str
    title: str
    date: str
    distance: float
    elevation_gain: float
    duration: float
    model_config = {"extra": "forbid"}


class ActivityCreate(BaseModel):
    activity_key: str
    activity_type: str
    title: str
    date: str
    distance: float = 0.0
    elevation_gain: float = 0.0
    duration: float = 0.0
    model_config = {"extra": "forbid"}


class ActivityUpdate(BaseModel):
    title: str = ""
    activity_type: str = ""
    date: str = ""
    distance: float = 0.0
    elevation_gain: float = 0.0
    duration: float = 0.0
    model_config = {"extra": "forbid"}
