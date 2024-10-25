"""
Text-to-Speech (TTS) provider abstraction and ElevenLabs implementation.
"""

import requests
from fastyrcore.config import Config
from fastyrcore.models.typing import TTSRequest, TTSResponse


class TTSProvider:
    """Base class for Text-to-Speech providers."""

    def synthesize(self, request: TTSRequest) -> TTSResponse:
        """
        Abstract method to synthesize text to audio.

        Args:
            request (TTSRequest): The input text to convert.

        Returns:
            TTSResponse: The synthesized audio.
        """
        raise NotImplementedError("TTS providers must implement the synthesize method.")


class ElevenLabsTTS(TTSProvider):
    """ElevenLabs implementation of the TTSProvider interface."""

    def synthesize(self, request: TTSRequest) -> TTSResponse:
        """
        Synthesizes text to audio using the ElevenLabs API.

        Args:
            request (TTSRequest): The input text.

        Returns:
            TTSResponse: The synthesized audio content.
        """
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": Config.ELEVENLABS_API_KEY,
        }
        data = {"text": request.text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
        response = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{Config.ELEVENLABS_VOICE_ID}",
            headers=headers, json=data
        )
        response.raise_for_status()
        return TTSResponse(audio=response.content)