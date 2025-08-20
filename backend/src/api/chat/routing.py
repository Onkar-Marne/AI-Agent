from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.db import get_session
from api.ai.agents import get_supervisor
from api.ai.schemas import EmailMessageSchema, SupervisorMessageSchema
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


# Invoke-WebRequest -Uri http://localhost:8080/api/chats/ -Method POST -Body '{"message":"Hello World"}' -ContentType "application/json"

# Invoke-WebRequest -Uri https://ai-agent-z625h.ondigitalocean.app/api/chats/ -Method POST -Body '{"message":"Hello World"}' -ContentType "application/json"

# Invoke-WebRequest -Uri https://ai-agent-z625h.ondigitalocean.app/api/chats/ -Method POST -Body '{"message":"Give me a summary of why its better to go out"}' -ContentType "application/json"

# Invoke-WebRequest -Uri http://localhost:8080/api/chats/ -Method POST -Body '{"message":"Give me a summary of why its better to go out"}' -ContentType "application/json"


@router.post("/", response_model=SupervisorMessageSchema)
def chat_create_message(payload:ChatMessagePayLoad, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    #response = generate_email_message(payload.message)
    #return response
    supe = get_supervisor()
    msg_data = { 
        "messages": [
            {"role": "user",
             "content": f"{payload.message}"
            },
        ]
    }
    result = supe.invoke(msg_data)
    if not result:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    messages = result.get("messages")
    if not messages:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    return messages[-1]

