import openai

openai.api_key = "YOUR_API_KEY"

def ask_ai(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

user_input = input("You: ")
print("AI:", ask_ai(user_input))
