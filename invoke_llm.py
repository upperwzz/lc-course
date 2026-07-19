from model_init import get_model

model = get_model(temperature=0.8)

# response = model.invoke("你是谁")
# response = model.invoke([
#     {"role": "user", "content": "你是谁"},
#     {"role": "assistant", "content": "我是一个助手"}
# ])
# print(response.model_dump_json(indent=2))
stream = model.stream("你是谁")
for chunk in stream:
    print(chunk.content, end="", flush=True)

