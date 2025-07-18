from openai import OpenAI

client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system","content":"you are a virtual assistant name jarvis,skilled in grnreal task like alexa and google cloud."},
        {"role":"user","content": "what is coding."}
    ]
)

print(completion.choice[0].message.content)