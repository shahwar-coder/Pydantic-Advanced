'''
Pydantic default_factory with datetime — Top Interview Q&A 🔥
Context:
Auto-generating timestamps using datetime.now
'''


'''
1. Why is default_factory=datetime.now preferred over default=datetime.now()?

Answer:
default=datetime.now() ❌
→ Executed once at class definition time
→ Same timestamp reused for all instances

default_factory=datetime.now ✔
→ Function is called each time a new instance is created
→ Each object gets a fresh timestamp

This avoids shared/static values.
'''


'''
2. Why do log1 and log2 have slightly different timestamps?

Answer:
Because datetime.now() is executed separately for each instance.

Even if objects are created quickly,
timestamps differ at microsecond level.

This proves default_factory runs per instance.
'''


'''
3. What happens if created_at is explicitly provided?

Answer:
default_factory is NOT triggered.

Example:
Log(message="Hi", created_at=some_time)

→ Provided value is used directly
→ default_factory is ignored

So:
default_factory only works when field is missing.
'''


'''
4. When should you use default_factory with datetime in real systems?

Answer:
- Logging systems (created_at)
- Audit fields (created_at, updated_at)
- Event tracking
- Database record timestamps

It ensures:
✔ Accurate creation time
✔ No manual timestamp handling
'''