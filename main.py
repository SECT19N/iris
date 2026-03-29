from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
import datetime

IrisApp = FastAPI()

@IrisApp.get("/")
async def Root():
    return {
        "Hello": "World",
        "Time": f"{datetime.datetime.now()}"
        }

@IrisApp.get("/scalar")
async def ScalarDocs():
    return get_scalar_api_reference(
        openapi_url = IrisApp.openapi_url,
        scalar_proxy_url = "https://proxy.scalar.com",
    )
