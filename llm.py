import os
import streamlit as st
from huggingface_hub import InferenceClient

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


def get_hf_token():
    """Read the Hugging Face token from Streamlit secrets or environment."""

    try:
        token = st.secrets.get("HF_TOKEN", "")
        if token:
            return token
    except Exception:
        pass

    return (
        os.getenv("HF_TOKEN")
        or os.getenv("HUGGINGFACEHUB_API_TOKEN")
        or ""
    )


def generate_response(prompt):
    """Generate a response using the Qwen instruction model."""

    token = get_hf_token()

    if not token:
        raise ValueError(
            "Hugging Face token not found. Add HF_TOKEN to "
            "your Streamlit secrets or environment variables."
        )

    client = InferenceClient(
    provider="featherless-ai",
    model=MODEL_NAME,
    api_key=token
)

    try:
        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Give accurate, clear, and well-organized answers."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as error:
        raise RuntimeError(
            f"Qwen response generation failed: {error}"
        ) from error
