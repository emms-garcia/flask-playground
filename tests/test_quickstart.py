# -*- coding: utf-8 -*-
import pytest
import os
import tempfile

from context import quickstart

@pytest.fixture
def client(request):
    quickstart.app.config['TESTING'] = True
    client = quickstart.app.test_client()
    return client
