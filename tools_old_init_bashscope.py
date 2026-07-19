import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_community.chat_models.tongyi import ChatTongyi

load_dotenv()

base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")

model = ChatTongyi(
    model="qwen3.7-plus",
    api_key=api_key,
    base_url=base_url
)

print(type(model))