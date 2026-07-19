from langchain.agents import create_agent

from model_init import get_model

model = get_model()
agent = create_agent(model=model)

# response = agent.invoke({
#     "messages": [
#         {"role": "user", "content": "你是谁"}
#     ]
# })

response = agent.stream({
    "messages": [
        {"role": "user", "content": "你是谁"}
    ]
},
    stream_mode="messages"
)

for chunk,metadata in response:
    if chunk.content:
        print(chunk.content, end="", flush=True)
