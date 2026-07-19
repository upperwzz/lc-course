from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

# 1. 创建模型对象（关键：在这里加上 verbose=True）
llm = ChatOpenAI(
    model="qwen3.7-plus",
    api_key=api_key,
    base_url="https://ws-si6irqdnm3df42tu.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    verbose=True,  # 开启大模型的详细日志
)

# 2. 定义工具
@tool
def get_weather(location: str) -> str:
    "获取指定城市的当前天气信息。"
    return f"{location} 的天气是：晴天，当前温度：25°C"

# 3. 创建 Agent（这里不再需要 verbose 参数）
agent = create_agent(llm, tools=[get_weather])

# 4. 触发执行
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "今天北京的天气如何？"}
    ]
})

# 打印最终结果
for item in response["messages"]:
    print(item.model_dump_json(indent=2))