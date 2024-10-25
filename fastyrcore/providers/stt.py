"""
Speech-to-Text (STT) provider abstraction and DeepGram implementation.
"""

from abc import ABC, abstractmethod
from fastyrcore.models.typing import STTRequest, STTResponse
import requests
from fastyrcore.config import Config


class STTProvider(ABC):
    """Base class for Speech-to-Text providers."""

    @abstractmethod
    def transcribe(self, request: STTRequest) -> STTResponse:
        """
        Abstract method to transcribe audio to text.

        Args:
            request (STTRequest): The input request containing the audio URL.

        Returns:
            STTResponse: The transcription result.
        """
        raise NotImplementedError("STT providers must implement the transcribe method.")


class DeepGramSTT(STTProvider):
    """DeepGram implementation of the STTProvider interface."""

    def transcribe(self, request: STTRequest) -> STTResponse:
        """
        Transcribes audio using the DeepGram API.

        Args:
            request (STTRequest): The input request containing the audio URL.

        Returns:
            STTResponse: The transcription result.
        """
        headers = {"Authorization": f"Token {Config.DEEPGRAM_API_KEY}"}
        payload = {"url": str(request.audio_url)}
        response = requests.post(
            "https://api.deepgram.com/v1/listen", headers=headers, json=payload
        )
        response.raise_for_status()
        transcript = response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
        return STTResponse(transcript=transcript)
