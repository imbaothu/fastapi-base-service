# follow https://docs.llama-api.com/essentials/chat

from openai import OpenAI

client = OpenAI(
    api_key="xxx",
    base_url="https://api.llama-api.com",
)

response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {
            "role": "system",
            "content": "Assistant is a large language model trained by OpenAI.",
        },
        {"role": "user", "content": "Who were the founders of Microsoft?"},
    ],
    stream=True
)

# print the chat completion
for event in response:
    print(response.choices)

# print(response)
# print(response.model_dump_json(indent=2))
# print(response.choices[0].message.content)
