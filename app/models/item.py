from pydantic import BaseModel

# Equivalente a un "schema" o "interface" en Node.js/TypeScript
class Item(BaseModel):
    name: str
    age: int
