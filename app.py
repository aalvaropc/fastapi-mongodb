from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
  title="FastApi/MongoDB",
  description="fastapi with mongoDB",
  version="1.0.0",
  openapi_tags=tags_metadata
)

app.include_router(user, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn

    host = "0.0.0.0"
    port = 8000
    uvicorn.run(app, host=host, port=port)
