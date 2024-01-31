import openai

class OpenAIModule:
    def __init__(self):
        self.api_key = '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'
        openai.api_key = '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'


    def process_input(self, user_input):
        # Process user input and generate response using GPT-3.5 model
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3.5 model
            prompt=user_input,
            max_tokens=100,  # Adjust as per your requirement
            temperature=0.7,  # Adjust as per your requirement
            n=1,  # Number of responses to generate
            stop=None,  # Stop generating response at a specific token
        )

        return response.choices[0].text.strip()
