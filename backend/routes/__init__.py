# ================================================================
# JFT API
# Description: FastAPI backend for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

from .root import router as root_router
from .activity import router as runners_router

routers = [root_router,
           runners_router]
