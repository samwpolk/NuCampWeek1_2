import openai
openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = "What is the weather like today?"

completions = openai.Completion.create(
    engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
message = completions.choices[0].text
print(message)
