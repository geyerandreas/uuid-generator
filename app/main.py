import datetime
import uuid
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    redoc_url=None,
    title="UUID Generator",
    description="A simple API to generate UUIDs",
)


class UUIDResponse(BaseModel):
    uuid: uuid.UUID
    version: int
    timestamp: datetime.datetime


@app.get("/uuid/v4")
def get_uuid_v4() -> UUIDResponse:
    return UUIDResponse(
        uuid=uuid.uuid4(),
        version=4,
        timestamp=datetime.datetime.now(datetime.timezone.utc),
    )
