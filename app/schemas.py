from pydantic import BaseModel, HttpUrl

# Example request schema
class ExampleRequestSchema(BaseModel):
    name: str
    age: int
    email: str

# Example response schema
class ExampleResponseSchema(BaseModel):
    success: bool
    message: str

# Additional schemas can be added here for other request/response formats.