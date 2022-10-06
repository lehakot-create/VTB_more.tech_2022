from pydantic import BaseModel
from typing import List


class Role(BaseModel):
    role: str


class Source(BaseModel):
    """
    Модель источников даннных RSS лент
    """
    name: str
    url: str


class ListSource(BaseModel):
    role: Role
    lstSource: List[Source]
