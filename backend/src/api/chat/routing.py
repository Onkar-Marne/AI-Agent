from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from .models import ChatMessagePayLoad, ChatMessage, ChatMessageListItem


router = APIRouter()


@router.get("/")
def chat_health():
    return {"status":"OK"}


@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results


# Invoke-WebRequest -Uri https://localhost:8080/api/chats/ -Method POST -Body '{"message":"Hello World"}' -ContentType "application/json"

# Invoke-WebRequest -Uri https://ai-agent-z625h.ondigitalocean.app/api/chats/ -Method POST -Body '{"message":"Hello World"}' -ContentType "application/json"

# Invoke-WebRequest -Uri https://localhost:8080/api/chats/ -Method POST -Body '{"message":"Give me a summary of why its better to go out ..."}' -ContentType "application/json"


@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(payload:ChatMessagePayLoad, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    #session.refresh(obj)
    response = generate_email_message(payload.message)
    return response