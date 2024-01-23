import openai

openai.api_key = 'ENTER_YOUR_OPENAI_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
