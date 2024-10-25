"""
Configuration module for loading API keys and environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to manage API keys for external providers."""

    DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
    ELEVENLABS_VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID')