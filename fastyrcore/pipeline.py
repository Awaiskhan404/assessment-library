"""
Pipeline module to orchestrate the AI phone call process using STT, LLM, and TTS providers.
"""

from fastyrcore.stt import STTProvider
from fastyrcore.llm import LLMProvider
from fastyrcore.tts import TTSProvider
from fastyrcore.models.typing import STTRequest, LLMRequest, TTSRequest


class AIPipeline:
    """
    AIPipeline orchestrates the entire AI phone call pipeline by integrating
    Speech-to-Text (STT), Language Model (LLM), and Text-to-Speech (TTS) providers.
    """

    def __init__(self, stt: STTProvider, llm: LLMProvider, tts: TTSProvider):
        """
        Initializes the AI pipeline with specific providers.

        Args:
            stt (STTProvider): The Speech-to-Text provider.
            llm (LLMProvider): The Language Model provider.
            tts (TTSProvider): The Text-to-Speech provider.
        """
        self.stt = stt
        self.llm = llm
        self.tts = tts

    def handle_call(self, audio_url: str) -> bytes:
        """
        Orchestrates the AI phone call process by converting audio to text,
        generating a response, and synthesizing the response into audio.

        Args:
            audio_url (str): The URL of the audio input.

        Returns:
            bytes: The synthesized audio response.
        """
        # Step 1: Transcribe audio
        stt_request = STTRequest(audio_url=audio_url)
        transcription = self.stt.transcribe(stt_request).transcript

        # Step 2: Generate LLM response
        llm_request = LLMRequest(prompt=transcription)
        response_text = self.llm.generate_response(llm_request).response

        # Step 3: Synthesize TTS audio
        tts_request = TTSRequest(text=response_text)
        audio_response = self.tts.synthesize(tts_request).audio

        return audio_response
