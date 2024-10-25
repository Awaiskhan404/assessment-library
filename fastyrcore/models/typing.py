"""
This module defines Pydantic models for input and output validation.
"""

from pydantic import BaseModel, HttpUrl, constr


class STTRequest(BaseModel):
    """Model for Speech-to-Text (STT) request."""
    audio_url: HttpUrl


class STTResponse(BaseModel):
    """Model for Speech-to-Text (STT) response."""
    transcript: str


class LLMRequest(BaseModel):
    """Model for Language Model (LLM) request."""
    prompt: constr(min_length=1)


class LLMResponse(BaseModel):
    """Model for Language Model (LLM) response."""
    response: str


class TTSRequest(BaseModel):
    """Model for Text-to-Speech (TTS) request."""
    text: constr(min_length=1)


class TTSResponse(BaseModel):
    """Model for Text-to-Speech (TTS) response."""
    audio: bytes
