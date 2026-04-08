'''
Pydantic Matrix Validator — Deep Interview Q&A (Concept + Depth 🔥)
Focus:
- Nested lists
- Custom validators
- Data integrity
- Edge cases
'''


'''
1. Why is a custom validator needed here if Pydantic already validates types?

Answer:
Pydantic only validates types (List[List[int]]).
It ensures:
- Outer structure is a list
- Inner elements are lists
- Values are integers

However, it does NOT enforce business rules like:
- Matrix should not be empty
- Rows should not be empty
- All rows must have equal length

Custom validators are required for such structural constraints.
'''


'''
2. What is the role of @field_validator("values") in this code?

Answer:
It attaches custom validation logic to the "values" field.

Execution flow:
- Pydantic first performs type validation
- Then calls this validator
- If any condition fails → raises ValueError → converted to ValidationError

So it acts as a second validation layer after type checking.
'''


'''
3. Why is @classmethod used with field_validator?

Answer:
Pydantic expects validator methods to be class methods.

Reason:
- Validators operate at class level, not instance level
- cls allows access to model metadata if needed

Even if cls is not used, it must be included.
'''


'''
4. What will happen if input is [] (empty matrix)?

Answer:
Validator will raise:
"Matrix cannot be empty"

Because:
if not v → True → ValueError raised

This prevents invalid empty structures from being accepted.
'''


'''
5. What happens if one row is empty like [[1, 2], []]?

Answer:
ValidationError is raised:
"Rows cannot be empty"

Because:
any(len(row) == 0 for row in v) → True

Ensures every row has at least one element.
'''


'''
6. Why do we check row_length = len(v[0])?

Answer:
To establish a reference row length.

Then compare all rows against it:
→ Ensures matrix is rectangular (not jagged)

Without this:
[[1, 2], [3]] would pass type validation but is structurally invalid.
'''


'''
7. What type of error is raised inside validator and what does Pydantic return?

Answer:
Inside validator:
→ ValueError is raised

Pydantic converts it into:
→ ValidationError (user-facing)

This standardizes error handling across the framework.
'''


'''
8. Does this validator run before or after type coercion?

Answer:
After type coercion (default mode).

Flow:
Input → Type parsing (e.g., "1" → 1) → Validator runs

So validator always receives already parsed/validated data.
'''


'''
9. How would you run validation BEFORE type conversion?

Answer:
Use:
@field_validator("values", mode="before")

This allows validation on raw input before parsing.

Use case:
- Preprocessing
- Rejecting certain raw formats early
'''


'''
10. Can this validator ensure matrix contains only positive numbers?

Answer:
Yes, by extending logic:

Example:
if any(num <= 0 for row in v for num in row):
    raise ValueError("Matrix must contain only positive numbers")

This shows validators can enforce both:
✔ Structure
✔ Value constraints
'''


'''
11. What happens if input is [["1", "2"], ["3", "4"]]?

Answer:
Pydantic will:
- Coerce strings → integers
- Then validator runs

Final result:
[[1, 2], [3, 4]] ✔ valid

Unless strict mode is enabled.
'''


'''
12. How would strict mode affect this matrix model?

Answer:
If strict=True:
- "1" will NOT be converted to int
- ValidationError will be raised before validator runs

Strict mode disables coercion.
'''


'''
13. What kind of error message does Pydantic provide for nested validation?

Answer:
Pydantic provides detailed error paths:

Example:
values -> 1 -> 0

Meaning:
- values list
- second row (index 1)
- first element (index 0)

This helps pinpoint exact failure location.
'''


'''
14. Is this validation efficient for large matrices?

Answer:
It is O(n*m) where:
- n = number of rows
- m = elements per row

Because:
- Iterates through all rows
- May iterate through all elements (if extended checks added)

For very large data:
→ Consider optimization or streaming validation
'''


'''
15. Real-world use cases of this pattern?

Answer:
- ML data validation (feature matrices)
- Spreadsheet-like data processing
- Image pixel grids
- Game boards / grids
- Scientific computations

Ensures data consistency before processing.
'''


'''
🔥 Interview Killer Insight:

"Pydantic ensures type correctness automatically,
but real-world data integrity (like matrix shape)
must be enforced using custom validators."

This is where junior vs senior understanding is exposed.
'''