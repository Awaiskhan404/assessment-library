"""
Language Model (LLM) provider abstraction and OpenAI implementation.
"""

import requests
from abc import ABC, abstractmethod
from fastyrcore.config import Config
from fastyrcore.models.typing import LLMRequest, LLMResponse


class LLMProvider(ABC):
    """Base class for Language Model providers."""

    @abstractmethod
    def generate_response(self, request: LLMRequest) -> LLMResponse:
        """
        Abstract method to generate a response from a given prompt.

        Args:
            request (LLMRequest): The input prompt.

        Returns:
            LLMResponse: The generated response.
        """
        raise NotImplementedError("LLM providers must implement the generate_response method.")


class OpenAILLM(LLMProvider):
    """OpenAI's implementation of the LLMProvider interface."""

    def generate_response(self, request: LLMRequest) -> LLMResponse:
        """
        Generates a response using the OpenAI API.

        Args:
            request (LLMRequest): The input prompt.

        Returns:
            LLMResponse: The generated response.
        """
        headers = {
            "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Tell me a joke!"}],
            "temperature": 0.7,
            "max_tokens": 150,
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        response_text = response.json()["choices"][0]["message"]["content"].strip()
        return LLMResponse(response=response_text)
