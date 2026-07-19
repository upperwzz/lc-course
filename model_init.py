# model_init.py
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 在模块加载时自动读取环境变量
load_dotenv()

def get_model(temperature: float = 0.7):
    """
    统一的模型初始化入口。
    后续所有的 Prompt、Tool、Runnable 都复用这一个实例。
    """
    return init_chat_model(
        model=os.getenv(".env", "qwen3.7-plus"),
        model_provider="openai",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL"),
        temperature=temperature,
        extra_body={
            "enable_thinking": False  # 关闭思考模式
        },
        timeout=30,
        max_retries=2,
    )