from sqlmodel import SQLModel, Field

class ChatMessagePayLoad(SQLModel):
    # pydantic model for validation
    # validation
    message: str

class ChatMessage(SQLModel, table=True):
    # database table
    # saving, updating, deleting, getting
    id: int | None = Field(default=None, primary_key=True)
    message: str