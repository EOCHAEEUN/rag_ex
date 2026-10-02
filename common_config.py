"""Compatibility imports for notebooks that use ``common_config`` directly."""

from config.common_config import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_EMBEDDING_MODEL,
    embedding_model,
    get_embeddings,
    get_llm,
    llm_connect,
    project_path,
)

__all__ = [
    "DEFAULT_CHAT_MODEL",
    "DEFAULT_EMBEDDING_MODEL",
    "embedding_model",
    "get_embeddings",
    "get_llm",
    "llm_connect",
    "project_path",
]
