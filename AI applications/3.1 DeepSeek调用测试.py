# from openai import OpenAI
#
# client = OpenAI(api_key="123", base_url="https://api.deepseek.com")
#
# response = client.responses.create(
#     model="deepseek-v4-flash",
#     instructions="You are a helpful assistant.",
#     input="你是什么模型",
# )
#
# print(response.output_text)

from openai import OpenAI

client = OpenAI(api_key="123", base_url="https://api.deepseek.com")

stream = client.responses.create(
    model="deepseek-v4-flash",
    instructions="You are a helpful assistant.",
    input="你是什么模型",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")