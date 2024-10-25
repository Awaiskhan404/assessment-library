"""
Test suite for the AIPipeline class using pytest.
"""

import pytest
from fastyrcore.pipeline import AIPipeline
from fastyrcore.stt import DeepGramSTT
from fastyrcore.llm import OpenAILLM
from fastyrcore.tts import ElevenLabsTTS
from fastyrcore.models.typing import STTRequest, LLMRequest, TTSRequest


@pytest.fixture
def ai_pipeline():
    """Fixture to initialize the AI pipeline with providers."""
    stt = DeepGramSTT()
    llm = OpenAILLM()
    tts = ElevenLabsTTS()
    return AIPipeline(stt, llm, tts)


def test_stt_transcription(ai_pipeline):
    """Test STT transcription with mock data."""
    audio_url = "https://example.com/sample-audio.wav"
    stt_request = STTRequest(audio_url=audio_url)
    response = ai_pipeline.stt.transcribe(stt_request)
    assert response.transcript, "Expected non-empty transcription."


def test_llm_response_generation(ai_pipeline):
    """Test LLM response generation with a sample prompt."""
    prompt = "Hello, how are you?"
    llm_request = LLMRequest(prompt=prompt)
    response = ai_pipeline.llm.generate_response(llm_request)
    assert response.response, "Expected non-empty LLM response."


def test_tts_synthesis(ai_pipeline):
    """Test TTS synthesis with a sample text."""
    text = "This is a test."
    tts_request = TTSRequest(text=text)
    response = ai_pipeline.tts.synthesize(tts_request)
    assert isinstance(response.audio, bytes), "Expected audio response in bytes."


def test_pipeline_end_to_end(ai_pipeline):
    """Test the end-to-end pipeline process."""
    audio_url = "https://example.com/sample-audio.wav"
    audio_response = ai_pipeline.handle_call(audio_url)
    assert isinstance(audio_response, bytes), "Expected audio response in bytes."


def test_invalid_audio_url(ai_pipeline):
    """Test the pipeline with an invalid audio URL."""
    with pytest.raises(ValueError):
        ai_pipeline.handle_call("invalid-url")