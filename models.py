from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Grocery(BaseModel):
     grocery_id: Optional[UUID] = uuid4()
     name: str
     brand: str
     origin: str
     quantity:str
     size: Optional[int]
    

class GroceriesUpdate(BaseModel):
     grocery_id: Optional[UUID] = uuid4()
     name: str
     brand: Optional[str]
     origin: Optional[str]
     quantity: Optional[str]
     size: Optional [int]

      
    