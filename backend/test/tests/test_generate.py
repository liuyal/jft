# ================================================================
# JFT API
# Description: FastAPI backend test script for the JFT application.
# Author: Jerry
# License: MIT
# ================================================================

import logging

import pytest

from .test_base import BaseTest


@pytest.mark.order(1)
class TestJftTMGenerate(BaseTest):

    def test_generate_mock_data(self, request):
        logging.info(f"--- Starting test: {request.node.name} ---")
        self.__class__.reset_db()

        logging.info(f"--- Test: {request.node.name} Complete ---")
