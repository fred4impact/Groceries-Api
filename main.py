from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID  #uuid4
from models import Grocery, GroceriesUpdate

app = FastAPI()

db: List[Grocery] = [
   Grocery(
        grocery_id = UUID("128e8662-386e-466e-8f95-a19ae9560ead"),
        name = "Bananas",
        brand = "chiquita ",
        origin = "Mexico",
        quantity = "40",
        size = 12, 
    ),
    Grocery(
        grocery_id = UUID("228e8662-386e-466e-8f95-a19ae9560eae"),
        name = "Peanut Butter",
        brand = "JIF ",
        origin = "Mexico",
        quantity = "30",
        size = 2, 
    ),
     Grocery(
        grocery_id = UUID("328e8662-386e-466e-8f95-a19ae9560eab"),
        name = "Wheat Bread",
        brand = "Oroweat ",
        origin = "Califonia",
        quantity = "100",
        size = 15, 
    ),
     Grocery(
        grocery_id = UUID("428e8662-386e-466e-8f95-a19ae9560eab"),
        name = "Greek yogurt",
        brand = "Fage ",
        origin = "Califonia",
        quantity = "5",
        size = 10, 
    ),
 
]


@app.get("/")
def index():
      return{"Message": "Welcome to Groceries FastAPI Resources "}


@app.get("/api/v1/groceries")
async def get_gorceries():
    return db;


@app.post("/api/v1/groceries")
async def create_grocery(grocery: Grocery):
    db.append(grocery)
    return {"groceryId": grocery.grocery_id};


@app.delete("/api/v1/groceries/{grocery_id}")
async def delete_grocery(grocery_id: UUID):
    for grocery in db: 
        if grocery.grocery_id == grocery_id:
            db.remove(grocery)
            return 
    raise HTTPException(
    status_code=404,detail=f"Grocery with GroceryId:{grocery_id} does not exists"
) 

    

@app.put("/api/v1/groceries/{grocery_id}")
async def update_grocery(grocery_update: GroceriesUpdate, grocery_id: UUID):
   for grocery in db:
        if grocery.grocery_id == grocery_id:
           if grocery_update.name is not None:
              grocery.fname  =  grocery_update.name
           if grocery_update.brand is not None:
               grocery.brand = grocery_update.brand 
           if grocery_update.origin is not None:
               grocery.origin = grocery_update.origin 
           if grocery_update.quantity is not None:
               grocery.quantity = grocery_update.quantity
           if grocery_update.size is not None:
               grocery.size = grocery_update.size 
           return 
   raise HTTPException(
    status_code=404, detail=f"Grocery with groceryId:{grocery_id} does not exists"
)       
