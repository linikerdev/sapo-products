import os

from app import create_app
import uvicorn

app = create_app(config="dev")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)