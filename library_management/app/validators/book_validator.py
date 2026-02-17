from pydantic import BaseModel
from typing import Optional



#logfire is used to monitor pydantic validations and understand why 
#some inputs fails validations
#import logfire
#logfire.configure()
#logfire.instrument_pydantic()  

class BookCreate(BaseModel):
    title: str
    author: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
