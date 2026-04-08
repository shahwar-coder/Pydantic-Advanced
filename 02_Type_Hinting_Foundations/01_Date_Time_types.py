from datetime import date, datetime, time
from pydantic import BaseModel, ValidationError

class Event(BaseModel):
    event_date: date
    event_time: time
    event_datetime: datetime


try:
    event = Event(
        event_date="2024-03-01",          # YYYY-MM-DD
        event_time="14:30:00",            # HH:MM:SS
        event_datetime="2024-03-01T14:30:00"  # ISO format
    )

    print("✅ Parsed Event:", event)

    print("\n--- Access Individual Fields ---")
    print("Date:", event.event_date)
    print("Time:", event.event_time)
    print("Datetime:", event.event_datetime)

except ValidationError as e:
    print("❌ Validation Error:")
    print(e)


# time(2024, 3, 1, 14, 30)

# --- Access Individual Fields ---
# Date: 2024-03-01
# Time: 14:30:00
# Datetime: 2024-03-01 14:30:00

# -=-=-=-=-=-=-=-=

'''
======================
📌 OVERALL PURPOSE
======================
This code demonstrates how Pydantic automatically:
1. Parses string inputs into proper Python date/time objects
2. Validates the correctness of those inputs
3. Provides structured access to the parsed data

It showcases Pydantic’s ability to handle:
- date
- time
- datetime
using standard string formats (ISO formats)

This is very important in APIs (e.g., FastAPI) where data comes as JSON strings.

======================
📌 STEP-BY-STEP FLOW
======================

1. IMPORTS
-----------
from datetime import date, datetime, time
→ Native Python types for handling date and time

from pydantic import BaseModel, ValidationError
→ BaseModel: used to define schema
→ ValidationError: raised if parsing/validation fails


2. MODEL DEFINITION
-------------------
class Event(BaseModel):
    event_date: date
    event_time: time
    event_datetime: datetime

→ A Pydantic model is defined with strict types:
   - event_date must be a date object
   - event_time must be a time object
   - event_datetime must be a datetime object

⚠️ Important:
Even though types are strict, Pydantic allows flexible input (like strings)
and converts them internally.


3. OBJECT CREATION (TRY BLOCK)
------------------------------
event = Event(
    event_date="2024-03-01",
    event_time="14:30:00",
    event_datetime="2024-03-01T14:30:00"
)

→ User provides STRING inputs (common in APIs)

→ Pydantic internally:
   - Detects expected type
   - Parses string into correct Python object

Internally happening:

"2024-03-01" → date(2024, 3, 1)
"14:30:00" → time(14, 30, 0)
"2024-03-01T14:30:00" → datetime(2024, 3, 1, 14, 30)

This process is called:
👉 Data Parsing + Validation


4. PRINTING FULL MODEL
----------------------
print("✅ Parsed Event:", event)

→ Pydantic prints a structured representation:
Event(event_date=..., event_time=..., event_datetime=...)

⚠️ This is NOT raw strings anymore — these are real Python objects.


5. ACCESSING INDIVIDUAL FIELDS
------------------------------
event.event_date
event.event_time
event.event_datetime

→ You can access fields like normal attributes

→ Types:
type(event.event_date) → datetime.date
type(event.event_time) → datetime.time
type(event.event_datetime) → datetime.datetime


6. ERROR HANDLING
-----------------
except ValidationError as e:

→ If any field:
   - Has wrong format
   - Is invalid
   - Cannot be parsed

Pydantic raises ValidationError

Example failure cases:
- event_date="2024/03/01" ❌ (wrong format)
- event_time="25:00:00" ❌ (invalid hour)
- event_datetime="invalid" ❌


======================
📌 INTERNAL EXECUTION FLOW
======================

Input (strings)
      ↓
Pydantic Model Initialization
      ↓
Type Inspection (date/time/datetime)
      ↓
Parsing Logic (ISO format parsing)
      ↓
Validation (is it valid date/time?)
      ↓
Converted Python Objects Stored
      ↓
Accessible via attributes


======================
📌 WHY THIS IS IMPORTANT (INTERVIEW GOLD)
======================

1. Real-world usage:
   - APIs receive strings → need structured types
   - Pydantic handles parsing automatically

2. Eliminates manual parsing:
   Without Pydantic:
   datetime.strptime(...) ❌ (manual & error-prone)

3. Strong validation layer:
   Prevents invalid data entering system

4. FastAPI integration:
   Request JSON → automatically converted into Python types


======================
📌 KEY TAKEAWAYS
======================

✔ Pydantic automatically converts strings → date/time/datetime  
✔ Uses ISO format by default  
✔ Raises ValidationError for invalid inputs  
✔ Makes data handling clean, safe, and structured  
✔ Extremely useful in backend/API development  

======================
📌 BONUS INSIGHT
======================

Pydantic v2 uses:
→ model_validate() internally for parsing
→ Faster validation using pydantic-core (Rust backend)

This is why parsing is both:
✔ Fast
✔ Reliable
'''