"""
Text-to-Speech (TTS) provider abstraction and ElevenLabs implementation.
"""

import requests
from abc import ABC, abstractmethod
from fastyrcore.config import Config
from fastyrcore.models.typing import TTSRequest, TTSResponse


class TTSProvider(ABC):
    """Base class for Text-to-Speech providers."""

    @abstractmethod
    def synthesize(self, request: TTSRequest, save_to: str = None) -> TTSResponse:
        """
        Abstract method to synthesize text to audio.

        Args:
            request (TTSRequest): The input text to convert.
            save_to (str): The path to save the audio file

        Returns:
            TTSResponse: The synthesized audio.
        """
        raise NotImplementedError("TTS providers must implement the synthesize method.")


class ElevenLabsTTS(TTSProvider):
    """ElevenLabs implementation of the TTSProvider interface."""

    def synthesize(self, request: TTSRequest, save_to: str = None) -> TTSResponse:
        """
        Synthesizes text to audio using the ElevenLabs API.

        Args:
            request (TTSRequest): The input text.
            save_to (str): The path to save the audio file.

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
        if save_to:
            # Save the audio mp3 to a file on given path
            with open(f"{save_to}.mp3", "wb") as f:
                f.write(response.content)
        response.raise_for_status()
        return TTSResponse(audio=response.content)
