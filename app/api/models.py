from pydantic import BaseModel
from typing import List, Optional

class CurrencyIn(BaseModel):
    name: str
    code: str
    max_count: str
    area: str


class CurrencyOut(CurrencyIn):
    id: int
