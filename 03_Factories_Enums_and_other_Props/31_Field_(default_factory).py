from pydantic import BaseModel, Field

from datetime import datetime

class Log(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)

print(Log())

# created_at=datetime.datetime(2026, 4, 10, 4, 7, 42, 274584)