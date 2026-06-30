from typing import List, Optional
from pydantic import BaseModel


class FieldConfig(BaseModel):
    path: str
    from_field: str
    type: str = "string"
    normalize: Optional[str] = None
    required: bool = False


class OutputConfig(BaseModel):
    fields: List[FieldConfig]
    include_confidence: bool = True
    on_missing: str = "null"