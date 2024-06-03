from typing import Optional

from pydantic import BaseModel


class StudentAdd(BaseModel):
    name: str
    description: Optional[str] = None

class Student(StudentAdd):
    id: int
