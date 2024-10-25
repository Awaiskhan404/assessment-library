# FastyrCore

An extensible and modular AI phone call pipeline library that integrates Speech-to-Text (STT), Language Models (LLM), and Text-to-Speech (TTS) capabilities. FastyrCore provides a consistent and intuitive API that allows developers to easily switch between different providers for each stage of the pipeline.

## Supported Providers
- **DeepGram (STT)**
- **OpenAI (LLM)**
- **ElevenLabs (TTS)**

## Features
- **Modular design**: Easily switch between providers.
- **Abstraction**: Common interfaces for each stage (STT, LLM, TTS).
- **Extensible**: Add new providers with minimal changes.
- **Provider-agnostic API**: Simplifies development by decoupling logic from specific providers.
- **Reusable components**: Easily integrate with other projects.

## Usage
```python
from fastyrcore.pipeline import AIPipeline
from fastyrcore.providers.stt import DeepGramSTT
from fastyrcore.providers.llm import OpenAILLM
from fastyrcore.providers.tts import ElevenLabsTTS

# Initialize the AI pipeline with specific providers
pipeline = AIPipeline(DeepGramSTT(), OpenAILLM(), ElevenLabsTTS())

# Handle an AI-powered phone call by providing an audio URL
audio_response = pipeline.handle_call("https://example.com/sample-audio.wav")

# Save the synthesized response as an audio file
with open("response.mp3", "wb") as f:
    f.write(audio_response)
```

## Project Structure
```
fastyrcore/
│
├── fastyrcore/
│   ├── __init__.py             # Package initializer
│   ├── config.py               # Configuration loader
│   ├── providers/              # Providers for STT, LLM, TTS
│   │   ├── __init__.py
│   │   ├── stt.py              # STT providers (e.g., DeepGram)
│   │   ├── llm.py              # LLM providers (e.g., OpenAI)
│   │   ├── tts.py              # TTS providers (e.g., ElevenLabs)
│   ├── models.py               # Pydantic models for data validation
│   ├── pipeline.py             # Core pipeline logic
│
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py        # Test cases for the pipeline
│
├── .env                        # Environment variables (API keys)
├── requirements.txt            # Dependencies
├── setup.py                    # Package setup
└── README.md                   # Documentation
```

## Providers

Speech-to-Text (STT) Providers

	•	DeepGramSTT: Uses DeepGram API to convert speech to text.
	•	To use a different STT provider, create a new class that implements the STTProvider interface.

Language Model (LLM) Providers

	•	OpenAILLM: Uses OpenAI’s API to generate text responses based on prompts.
	•	You can integrate other LLMs by implementing the LLMProvider interface.

Text-to-Speech (TTS) Providers

	•	ElevenLabsTTS: Uses ElevenLabs API to synthesize audio from text.
	•	To add other TTS providers, implement the TTSProvider interface.

## Pipeline

The AIPipeline class orchestrates the entire phone call pipeline by integrating the three stages:

	1.	STT: Converts audio input to text.
	2.	LLM: Generates a response based on the transcript.
	3.	TTS: Converts the response text back to audio.

The pipeline allows easy switching of providers using dependency injection.

## Contact

For any inquiries, feel free to reach out:

	•	Author: Awais khan
	•	Email: contact@awaiskhan.com.pk
	•	GitHub: Awaiskhan404