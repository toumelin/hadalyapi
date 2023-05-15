from typing import List
from pydantic import BaseModel


class Indicators(BaseModel):
    indicators: List[str]
    symbol: str
    start_date: str
    end_date: str
    interval: str

    #symbol: str, start_date: str, end_date: str, interval: str, pattern: str