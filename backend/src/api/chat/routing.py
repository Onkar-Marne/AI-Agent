from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session
from .models import ChatMessagePayLoad, ChatMessage


router = APIRouter()


@router.get("/")
def chat_health():
    return {"status":"OK"}


@router.get("/recent/")
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10]
    return results


@router.post("/", response_model=ChatMessage)
def chat_create_message(payload:ChatMessagePayLoad, session: Session = Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj