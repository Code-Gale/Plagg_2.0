import openai

openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
