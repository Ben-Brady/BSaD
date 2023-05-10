from typing import Literal
from dataclasses import dataclass

valid_roles = ["application", "operations", "resiliency", "admin"]
Role = Literal["application", "operations", "resiliency", "admin"]

@dataclass
class User:
    id: str
    name: str
    password: str
    role: Role
