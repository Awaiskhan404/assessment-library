from pydantic import BaseModel, HttpUrl, constr


class STTRequest(BaseModel):
    audio_url: HttpUrl


class STTResponse(BaseModel):
    transcript: str


class LLMRequest(BaseModel):
    prompt: constr(min_length=1)


class LLMResponse(BaseModel):
    response: str


class TTSRequest(BaseModel):
    text: constr(min_length=1)


class TTSResponse(BaseModel):
    audio: bytes
