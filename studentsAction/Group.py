from typing import Optional

from pydantic import BaseModel

from studentsAction.Student import Student


class GroupAdd(BaseModel):
    name: str
    description: Optional[set[Student]] = None

class Group(GroupAdd):
    id: int