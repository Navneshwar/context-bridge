"""Core data models for context-bridge."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum


class MemoryType(str, enum.Enum):
    DECISION = "decision"
    PATTERN = "pattern"
    LESSON = "lesson"
    PREFERENCE = "preference"
    ARCHITECTURE = "architecture"


class Memory(BaseModel):
    id: Optional[int] = None
    content: str
    memory_type: MemoryType
    source_agent: str  # claude, codex, opencode, hermes, aider
    session_id: str
    project_path: str
    relevance_score: float = 0.0
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    access_count: int = 0
    importance: float = 0.5


class Session(BaseModel):
    id: Optional[int] = None
    session_id: str
    agent: str
    project_path: str
    file_path: str
    content: str
    indexed: bool = False
    created_at: datetime = datetime.utcnow()


class Query(BaseModel):
    text: str
    agent: Optional[str] = None
    memory_type: Optional[MemoryType] = None
    limit: int = 10
