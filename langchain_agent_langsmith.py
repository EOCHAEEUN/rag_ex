from langchain.agents import create_agent
import os
import sys
from config.common_config import get_llm    
from dotenv import load_dotenv
load_dotenv(override=True, dotenv_path="../.env")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


llm = get_llm()

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "서울의 날씨를 알려줘."
            }
        ]
    }
)

print(result["messages"][-1].content)