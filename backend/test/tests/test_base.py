# ================================================================
# JFT API
# Description: FastAPI backend test script for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

import logging

import pytest
import requests


class BaseTest:
    """Base class for backend tests."""

    @classmethod
    def setup_class(cls):
        """Initialize test class"""

        logging.debug(f"Initialize tests...")

        cls.host = pytest.options['host']
        cls.port = pytest.options['port']

        cls.protocol = "http"
        cls.url = f"{cls.protocol}://{cls.host}:{cls.port}/api/v1"

        cls.session = requests.Session()

        response = cls.session.get(f"{cls.protocol}://{cls.host}:{cls.port}/")
        assert response.status_code == 204

    @classmethod
    def teardown_class(cls):
        """Teardown test class"""

        logging.debug(f"Teardown tests...")
        cls.session.close()

    @classmethod
    def reset_db(cls):
        """Reset the database"""

        response = cls.session.post(f"{cls.url}/reset-database", params={"db_name": "ALL"})
        assert response.status_code == 204
