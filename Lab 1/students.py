"""
Data module utilizing Pydantic v2 for data validation and robust type safety.
Updated for Python 3.12 compatibility.
"""

from typing import List
from pydantic import BaseModel, Field, field_validator

class Student(BaseModel):
    name: str = Field(..., min_length=2, description="Student full name")
    score: float = Field(..., ge=0.0, le=100.0, description="Score between 0 and 100")

    @field_validator('score')
    @classmethod
    def round_score(cls, v: float) -> float:
        return round(v, 2)

# Initial seed data for student records
INITIAL_STUDENTS: List[Student] = [
    Student(name="Marvelous Kalu", score=88.5),
    Student(name="Ayomirinde Oluwagbemiro", score=74.0),
    Student(name="Blessing Beanamaz", score=92.5),
    Student(name="Abazie Uchechukwu", score=65.0)
]

def get_student_dicts() -> List[dict]:
    """Returns raw dictionary representations for legacy compatibility."""
    return [s.model_dump() for s in INITIAL_STUDENTS]