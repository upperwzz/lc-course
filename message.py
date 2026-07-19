from dashscope.agentstudio.types import BaseModel
from debugpy.adapter.components import Capabilities
from langchain.agents import create_agent
from langchain_classic.chains.question_answering.map_reduce_prompt import messages

from model_init import get_model
from pydantic import BaseModel

system_prompt = """
# 身份
-你是一名程序员

# 指令
- 请用中文回答问题
- 不要返回表情符号

}

    
"""

class Capabilities(BaseModel):
    title: str
    content: str

model = get_model()
agent = create_agent(
    model=model,
    system_prompt=system_prompt,
    response_format=Capabilities
)

# messages = [
#     {
#     "role": "user",
#     "content": [
#         {"type": "text", "text": "描述下这张图片"},
#         {"type": "image", "image": "https://img0.baidu.com/it/u=3591665277,2616537962&fm=253&app=138&f=JPEG?w=800&h=1333"}
#         ]
#     }
# ]

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "如何学习python"}
        ]
    }
]

response = agent.invoke({"messages": messages})

print(response['structured_response'].title, response['structured_response'].content)


# stream = agent.stream(
#     {"messages": messages},
#     stream_mode="messages"
# )
#
# for token,metadata in stream:
#     if token.content:
#         print(token.content, end="", flush=True)