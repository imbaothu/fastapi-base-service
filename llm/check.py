from llama_index.llms.openai import OpenAI

llm = OpenAI()
resp = llm.stream_complete("Paul Graham is ")

for r in resp:
    print(r.delta, end="")