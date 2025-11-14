from __future__ import annotations
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class Booking(BaseModel):
    name: Optional[str] = None
    preferred_date: Optional[str] = None  # "2025-11-20"
    preferred_time: Optional[str] = None  # "14:00"
    topic: Optional[str] = None           # "Resume review"
    status: Literal["pending", "confirmed", "cancelled"] = "pending"


class SessionNotes(BaseModel):
    student: Optional[str] = None
    date: Optional[str] = None
    summary: Optional[str] = None
    action_items: List[str] = Field(default_factory=list)


class Feedback(BaseModel):
    student: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None


class EventInfo(BaseModel):
    query: Optional[str] = None
    result: Optional[str] = None


class GraphState(BaseModel):
    messages: List[Message] = Field(default_factory=list)
    intent: Optional[str] = None

    booking: Optional[Booking] = None
    notes: Optional[SessionNotes] = None
    feedback: Optional[Feedback] = None
    event: Optional[EventInfo] = None
    user_id: Optional[str] = None
    conversation_id: Optional[str] = None

    last_reply: Optional[str] = None
