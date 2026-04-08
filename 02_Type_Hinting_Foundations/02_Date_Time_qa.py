'''
Pydantic Date/Time Parsing — Top Interview Q&A (High Signal 🔥)
Context:
Pydantic parses string inputs into Python date, time, and datetime objects.
'''


'''
1. How does Pydantic handle date, time, and datetime fields when given string inputs?

Answer:
Pydantic automatically parses string inputs into corresponding Python objects
based on type hints.

Examples:
"2024-03-01" → date(2024, 3, 1)
"14:30:00" → time(14, 30, 0)
"2024-03-01T14:30:00" → datetime(2024, 3, 1, 14, 30)

This works because Pydantic supports ISO format parsing by default.
'''


'''
2. Why is this feature important in real-world backend systems?

Answer:
- APIs usually receive data as strings (JSON)
- Pydantic automatically converts them into structured Python objects
- Eliminates need for manual parsing (e.g., datetime.strptime)
- Reduces bugs and improves data consistency

This is especially critical in FastAPI-based systems.
'''


'''
3. What happens internally when you pass a string to a datetime field?

Answer:
Internal flow:
1. Input string received
2. Pydantic inspects expected type (datetime)
3. Applies parsing logic (ISO format)
4. Validates correctness
5. Stores as Python datetime object

If parsing fails → ValidationError is raised
'''


'''
4. What kind of inputs will cause ValidationError?

Answer:
- Incorrect format:
  "2024/03/01" ❌

- Invalid values:
  "25:00:00" ❌ (invalid hour)

- Completely invalid string:
  "random_text" ❌

Pydantic ensures both:
✔ Format correctness
✔ Logical validity
'''


'''
5. How can you verify that parsing actually converted values?

Answer:
By checking types:

type(event.event_date) → datetime.date
type(event.event_time) → datetime.time
type(event.event_datetime) → datetime.datetime

This confirms that values are no longer strings,
but proper Python objects.
'''


'''
6. What is the difference between parsing and validation in this context?

Answer:
Parsing:
- Converting input (string → Python object)

Validation:
- Ensuring the parsed value is correct and valid

Example:
"2024-03-01" → parsed ✔ valid ✔
"2024-02-30" → parsed ✔ but invalid ❌ (fails validation)

Both steps are handled automatically by Pydantic.
'''


'''
7. How does Pydantic improve developer productivity here?

Answer:
- Removes need for manual parsing logic
- Reduces boilerplate code
- Provides automatic error handling
- Ensures clean and consistent data structures

This leads to faster and safer backend development.
'''


'''
🔥 Interview Killer Insight:

"Pydantic bridges the gap between raw JSON input (strings)
and strongly typed Python objects by combining parsing
and validation in a single step."

'''