'''
Pydantic Serialization / Deserialization / Schema — Top Interview Q&A 🔥
References:
- model_dump / JSON 
- include/exclude 
- JSON schema 
- model_validate 
'''


'''
1. What is the difference between model_dump() and model_dump_json()?

Answer:
model_dump():
→ Returns Python dict
→ Keeps Python types (e.g., datetime object)

model_dump_json():
→ Returns JSON string
→ Converts types (datetime → ISO string)

Key idea:
dump → Python representation
dump_json → serialized (API-ready) format
'''


'''
2. How do include and exclude work in model_dump()?

Answer:
They control which fields are returned.

include={"name", "email"}:
→ Only selected fields included

exclude={"age"}:
→ Removes specific fields

Important:
Used for:
✔ API responses
✔ Hiding sensitive data
✔ Partial serialization

This is very common in real systems.
'''


'''
3. What is model_json_schema() and why is it important?

Answer:
It generates a JSON Schema from the model.

Used for:
- API documentation (FastAPI / OpenAPI)
- Validation contracts
- Frontend-backend communication

Key insight:
Pydantic → automatically defines API structure
without manual schema writing.
'''


'''
4. What is the difference between model_validate() and normal initialization?

Answer:
User(...) → direct model creation

model_validate(data):
→ Explicit validation from external data (dict)

model_validate_json(json_str):
→ Parses JSON string → model

Use cases:
✔ Parsing API input
✔ Data ingestion pipelines

This is called deserialization.
'''


'''
5. What is serialization vs deserialization in Pydantic?

Answer:
Serialization:
→ Model → dict / JSON
→ model_dump(), model_dump_json()

Deserialization:
→ dict / JSON → Model
→ model_validate(), model_validate_json()

Flow:
API input → deserialize → process → serialize → response

This full cycle is critical in backend systems.
'''


'''
🔥 Interview Killer Insight:

"Pydantic sits at the boundary of your system —
handling both serialization (output)
and deserialization (input) with strong validation."

This is why it is central in FastAPI.
'''