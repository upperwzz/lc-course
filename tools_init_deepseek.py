import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 1. 从 .env 文件加载环境变量（推荐的安全做法）
load_dotenv()

# 2. 初始化模型
model = init_chat_model(
    model="deepseek-chat",           # 模型名称
    # model_provider="deepseek",       # 显式指定服务商为 DeepSeek
    # api_key=os.getenv("DEEPSEEK_API_KEY"), # 传入 API 密钥
    # temperature=0.7,                 # 可选：控制随机性
    # max_tokens=2048                  # 可选：最大生成 Token 数
)

# 3. 打印模型对象
print(type(model))