"""Shared model configuration for every notebook in this repository."""

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

DEFAULT_CHAT_MODEL = "gpt-5.4-mini"
DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"


def _first_env(*names: str) -> str | None:
    """Return the first configured environment variable from ``names``."""
    return next((value for name in names if (value := os.getenv(name))), None)


def _api_settings() -> tuple[str, str | None]:
    """Resolve current and legacy environment-variable names consistently."""
    api_key = _first_env(
        "MONOROUTER_API_KEY",
        "LLM_API_KEY",
        "OPENAI_API_KEY",
    )
    base_url = _first_env(
        "MONOROUTER_BASE_URL",
        "LLM_BASE_URL",
        "OPENAI_BASE_URL",
    )

    if not api_key:
        raise ValueError(
            "API 키가 설정되어 있지 않습니다. "
            f"{ENV_PATH}에 MONOROUTER_API_KEY를 설정해주세요."
        )

    return api_key, base_url


def project_path(*parts: str) -> Path:
    """Return a path anchored at the repository root, independent of notebook CWD."""
    return BASE_DIR.joinpath(*parts)


def get_llm(
    model: str = DEFAULT_CHAT_MODEL,
    temperature: float = 0,
    max_tokens: int = 512,
    api_key: str | None = None,
) -> ChatOpenAI:
    """Create a chat model using the repository's shared API settings."""
    configured_api_key, base_url = _api_settings()
    return ChatOpenAI(
        model=model,
        api_key=api_key or configured_api_key,
        base_url=base_url,
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False if base_url else None,
    )


def get_embeddings(
    model: str = DEFAULT_EMBEDDING_MODEL,
) -> OpenAIEmbeddings:
    """Create an embedding model using the same API settings as the chat model."""
    api_key, base_url = _api_settings()
    return OpenAIEmbeddings(
        model=model,
        api_key=api_key,
        base_url=base_url,
    )


# Backward-compatible names used by the existing RAG notebooks.
llm_connect = get_llm
embedding_model = get_embeddings


__all__ = [
    "DEFAULT_CHAT_MODEL",
    "DEFAULT_EMBEDDING_MODEL",
    "embedding_model",
    "get_embeddings",
    "get_llm",
    "llm_connect",
    "project_path",
]
