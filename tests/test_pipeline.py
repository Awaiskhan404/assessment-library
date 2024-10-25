"""
Unit tests for the FastyrCore AI pipeline.
"""

import unittest
from fastyrcore.pipeline import AIPipeline
from fastyrcore.providers.stt import DeepGramSTT
from fastyrcore.providers.llm import OpenAILLM
from fastyrcore.providers.tts import ElevenLabsTTS
from fastyrcore.models.typing import STTRequest, LLMRequest, TTSRequest


class TestAIPipeline(unittest.TestCase):
    """Test suite for the AI pipeline."""

    def setUp(self):
        """Initialize the AI pipeline with mock providers."""
        self.pipeline = AIPipeline(DeepGramSTT(), OpenAILLM(), ElevenLabsTTS())

    def test_stt_transcription(self):
        """Test that the STT provider returns a non-empty transcript."""
        request = STTRequest(audio_url="https://www.kozco.com/tech/LRMonoPhase4.wav")
        response = self.pipeline.stt.transcribe(request)
        expected = "this is my voice on the left this is my voice on the left hand side this is my voice on the left this is my voice on the right this is my voice on the right hand side this is my voice on the right this is my voice in the center this is my voice coming from both left and right this is my voice in the center my voice will be out of phase on three one two"
        self.assertEqual(response.transcript, expected, "Expected transcript mismatch")

    def test_llm_response_generation(self):
        """Test that the LLM provider generates a valid response."""
        request = LLMRequest(prompt="Hello, how are you?")
        response = self.pipeline.llm.generate_response(request)
        self.assertTrue(response.response, "Expected non-empty LLM response")

    def test_tts_synthesis(self):
        """Test that the TTS provider returns audio data in bytes."""
        request = TTSRequest(text="Hello how are you this is test")
        response = self.pipeline.tts.synthesize(request)
        self.assertIsInstance(response.audio, bytes, "Expected audio response in bytes")

    def test_pipeline_end_to_end(self):
        """Test the entire pipeline from audio to audio response."""
        audio_url = "https://www.kozco.com/tech/LRMonoPhase4.wav"
        response_audio = self.pipeline.handle_call(audio_url)
        self.assertIsInstance(response_audio, bytes, "Expected audio response in bytes")

    def test_invalid_audio_url(self):
        """Test that an invalid audio URL raises an exception."""
        with self.assertRaises(ValueError):
            self.pipeline.handle_call("invalid-url")


if __name__ == "__main__":
    unittest.main()