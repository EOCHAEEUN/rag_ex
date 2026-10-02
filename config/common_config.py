import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# 프로젝트 루트의 .env 경로를 명시적으로 지정
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


# MonoRouter 설정
_API_KEY = os.getenv("MONOROUTER_API_KEY")
_BASE_URL = os.getenv("MONOROUTER_BASE_URL")


def get_llm(
    model: str,
    temperature: float = 0,
    max_tokens: int = 512,
) -> ChatOpenAI:

    if not _API_KEY:
        raise ValueError(
            "MONOROUTER_API_KEY가 설정되어 있지 않습니다. "
            f".env 경로를 확인해주세요: {ENV_PATH}"
        )

    if not _BASE_URL:
        raise ValueError(
            "MONOROUTER_BASE_URL이 설정되어 있지 않습니다. "
            f".env 경로를 확인해주세요: {ENV_PATH}"
        )

    return ChatOpenAI(
        model=model,
        api_key=_API_KEY,
        base_url=_BASE_URL,
        temperature=temperature,
        max_tokens=max_tokens,
        use_responses_api=False,
    )