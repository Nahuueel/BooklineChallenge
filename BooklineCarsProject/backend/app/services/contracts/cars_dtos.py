import datetime
from typing import List
from pydantic import BaseModel # type: ignore

class car_dto_response(BaseModel):
    name: str
    booked_dates: List[datetime.date] = list()