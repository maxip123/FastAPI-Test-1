from fastapi import APIRouter
from app.models.item import Item

# APIRouter es el equivalente a express.Router()
router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}
