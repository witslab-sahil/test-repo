"""Basic FastAPI application used to exercise the CI/CD pipeline."""
import os

from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "test-repo")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def root():
    return {"app": APP_NAME, "version": APP_VERSION, "message": "Hello from FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}
