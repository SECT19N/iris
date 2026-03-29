from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/")
async def Root():
    return { "Hello": "World" }

@app.get("/scalar")
async def ScalarDocs():
    return get_scalar_api_reference(
        openapi_url = app.openapi_url,
        scalar_proxy_url = "https://proxy.scalar.com",
    )
