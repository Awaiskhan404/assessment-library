#!/bin/bash

# Set environment variables
export DEEPGRAM_API_KEY="your_deepgram_api_key"
export OPENAI_API_KEY="your_openai_api_key"
export ELEVENLABS_API_KEY="your_elevenlabs_api_key"
export ELEVENLABS_VOICE_ID="your_voice_id"

# Run the unit tests
python tests/test_pipeline.py