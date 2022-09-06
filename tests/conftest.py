import asyncio
import os
import sys
from asyncio import Future
from typing import Generator, Any

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from app.run import app


def async_run_new_loop(future: Future):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(future)
    loop.close()


@pytest.fixture(scope="session", name="app")
def app_() -> FastAPI:
    async_run_new_loop(app.router.startup())
    yield app
    async_run_new_loop(app.router.shutdown())


@pytest.fixture
async def client() -> Generator[AsyncClient, Any, None]:
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client
