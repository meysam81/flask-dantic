import pytest
from flask import Flask


@pytest.fixture
def app():
    app = Flask("test_app")
    app.config["DEBUG"] = True
    app.config["TESTING"] = True

    return app
