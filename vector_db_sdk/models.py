from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class ChunkMetadata(BaseModel):
    name: str
    createdAt: str

class LibraryMetadata(BaseModel):
    name: str
    createdAt: str  # ISO 8601 string
    description: Optional[str] = None

class DocumentMetadata(BaseModel):
    name: str
    createdAt: str  # ISO 8601 string

class Library(BaseModel):
    id: Optional[str] = None  # Auto-generated by server
    name: str
    metadata: LibraryMetadata

class Document(BaseModel):
    id: Optional[str] = None  # Auto-generated by server
    metadata: DocumentMetadata

class Chunk(BaseModel):
    id: Optional[str] = None  # Auto-generated by server
    text: str
    metadata:ChunkMetadata
    #embedding: List[float]

    @classmethod
    def validate_embedding(cls, v):
        if len(v) != 1024:
            raise ValueError("Embedding must be 1024-dimensional")
        return v