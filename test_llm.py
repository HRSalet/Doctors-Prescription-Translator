from utils.llm import llm

response = llm.invoke(
    "Explain what PCM 650 medicine means."
)

print(response)