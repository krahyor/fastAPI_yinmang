from pydantic import BaseModel, Field
from typing import Optional
from yinmang.utils import AllOptional, PydanticObjectId
from yinmang.schemas.base_schema import BaseSchema, BaseSchemaInfo

import datetime


class BaseStudents(BaseSchema):
    first_name: str | None = None
    last_name: str | None = None
    weight: float | None = None
    height: float | None = None


class ResponseStudents(BaseStudents):
    id: PydanticObjectId = Field(alias="_id", serialization_alias="id")