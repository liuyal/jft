# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

# app/app_def.py

import os
import pathlib
from dataclasses import dataclass, field
from typing import Optional

from dotenv import load_dotenv


@dataclass
class DBIndex:
    keys: list[tuple[str, int]]
    index_name: str


@dataclass
class DBCollection:
    name: str
    schema: Optional[dict] = field(default_factory=dict)
    index: Optional[DBIndex] = None


@dataclass
class DB:
    name: str
    collections: list[DBCollection]


# Global Constants
API_VERSION = "v1"

# Directories
ROOT_DIR = pathlib.Path(__file__).parents[2]
BACKEND_DIR = pathlib.Path(__file__).parents[1]
TMP_DIR = BACKEND_DIR / 'tmp'
TMP_DIR.mkdir(parents=True, exist_ok=True)

# Load environment variables from .env file
if not (ROOT_DIR / 'env' / '.env').exists():
    raise Exception("Environment file .env not found in env directory.")

load_dotenv(ROOT_DIR / 'env' / '.env')

# MongoDB Connection Details
MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost").strip()
MONGODB_PORT = os.getenv("MONGODB_PORT", "27017").strip()
MONGODB_USER = os.getenv("MONGODB_USER", "admin").strip()
MONGODB_PASS = os.getenv("MONGODB_PASS", "password").strip()
MONGODB_URL = f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}:{MONGODB_PORT}"

# DB Constants
DB_CORE = "jft"
DB_NAME_ACTIVITY = f"{DB_CORE}-activity"

# DB COLLECTIONS
DB_COLLECTION_ACTIVITY = DBCollection(name="activity")

# DB Configs
DB_NAME_JFT = DB(
    name=f"{DB_CORE}-activity",
    collections=[DB_COLLECTION_ACTIVITY]
)

# DB Mapping
DB_ALL = [DB_NAME_JFT]
