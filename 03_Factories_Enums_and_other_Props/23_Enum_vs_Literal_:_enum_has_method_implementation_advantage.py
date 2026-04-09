from enum import Enum

class Role(str, Enum):
    admin = "admin"
    user = "user"

    def is_admin(self):
        return self == "admin"


role = Role.admin

print(role)              # Role.admin
print(role.is_admin())   # ✅ True


# Role is a class
# 👉 So it can have a method