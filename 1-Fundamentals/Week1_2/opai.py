import openai

# Set up the OpenAI API client
openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "Write a short story about a young boy who discovers a magical power."

response = openai.Completion.text(
    engine=model_engine, prompt=prompt, max_tokens=1024, temperature=0.5)
print(response)
