from dataclasses import dataclass

additional_fields = []

@dataclass
class TestingRecord:
    id: str
    name: str
    primary_location: str
    alternate_location: str
    application_staff_allocated: list[str]
    operation_staff_allocated: list[str]
    additional_information: dict[str, str]
