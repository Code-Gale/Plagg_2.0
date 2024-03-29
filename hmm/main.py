from openai import OpenAI

client = OpenAI(api_key='')

# Set up your OpenAI API key

# Define a function to generate a response from the chatbot
def generate_response(user_input):
    response = client.completions.create(
        model="gpt-3.5-turbo-0125", 
        prompt=user_input,
        max_tokens=100,
        temperature=0.7,
        n=1, 
        stop=None,
        timeout=10
    )
    return response.choices[0].text.strip()

# Main loop to interact with the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
        
    response = generate_response(user_input)
    print("Chatbot:", response)