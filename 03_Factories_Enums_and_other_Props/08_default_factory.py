from pydantic import BaseModel, Field
from datetime import datetime


class Log(BaseModel):
    message: str
    created_at: datetime = Field(default_factory=datetime.now)


log1 = Log(message="Start process")
log2 = Log(message="End process")

print(log1)
print(log2)

# message='Start process' created_at=datetime.datetime(2026, 4, 9, 13, 53, 33, 433316)
# message='End process' created_at=datetime.datetime(2026, 4, 9, 13, 53, 33, 433484)

'''
======================
📌 OVERALL PURPOSE
======================
Shows how to auto-generate timestamps using
default_factory in Pydantic.

======================
📌 CORE CONCEPTS
======================

created_at: datetime = Field(default_factory=datetime.now)

→ datetime.now:
   - Called at object creation time
   - Generates current timestamp

→ default_factory:
   - Ensures a fresh value per instance

======================
📌 EXECUTION FLOW
======================

log1 = Log(...)
→ created_at not provided
→ datetime.now() runs → timestamp assigned

log2 = Log(...)
→ datetime.now() runs again → new timestamp

⚠️ Each instance gets a slightly different time

======================
📌 OUTPUT
======================

log1.created_at ≠ log2.created_at

→ Difference is in microseconds

======================
📌 KEY TAKEAWAYS
======================

✔ default_factory generates dynamic timestamps  
✔ Runs separately for each object  
✔ Useful for logs, audit fields, tracking  

======================
📌 INTERVIEW INSIGHT
======================

default=datetime.now() ❌ (same timestamp for all)

default_factory=datetime.now ✔ (fresh timestamp each time)

'''