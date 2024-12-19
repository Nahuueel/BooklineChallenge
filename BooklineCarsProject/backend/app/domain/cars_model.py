import datetime
import logging
from typing import List
from pydantic import BaseModel # type: ignore

class car_model(BaseModel):
    id: int
    name: str
    booked_dates: List[datetime.date] = list()

    async def check_car_boking(self, specified_date: datetime.date) -> bool:
        logging.debug("check_car_boking executting...")
        for booked_date in self.booked_dates:
            if booked_date == specified_date:
                return True
        return False
    
    async def book_car(self, booking_date: datetime.date) -> bool:
        logging.debug("book_car executting...")
        if await self.check_car_boking(booking_date):
            return False
        self.booked_dates.append(booking_date)
        return True
    