import os
from fastapi import FastAPI
from .config import get_config
from .router import register_routes
from fastapi.middleware.cors import CORSMiddleware


    
def create_app(config="dev"):
    settings = get_config(config=config)

    app = FastAPI(title="SAPO API")
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_routes(app)

    return app