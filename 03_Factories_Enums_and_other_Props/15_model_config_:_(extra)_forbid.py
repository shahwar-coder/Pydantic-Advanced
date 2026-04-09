from pydantic import BaseModel, ConfigDict, ValidationError

class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str

try:
    user = User(name="Rahul", age=25)
except ValidationError as e:
    print(e)


# Extra inputs are not permitted [type=extra_forbidden, input_value=25, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/extra_forbidden