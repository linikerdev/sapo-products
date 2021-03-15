import os
from fastapi import FastAPI
from .config import get_config
from .router import register_routes

def create_app(config="dev"):
    settings = get_config(config=config)

    app = FastAPI(title="SAPO API")

    register_routes(app)

    @app.get("/")
    def index():
        return settings.CONFIG_NAME

    return app