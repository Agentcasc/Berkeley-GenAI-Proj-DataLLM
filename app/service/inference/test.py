import openai

def test():
    return "Hello, World! How are you"

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def openai_string_response(input):
    content = "You are a TA for a math class."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": content,
            },
            {
                "role": "user",
                "content": f"{input}",
            }
        ],
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the assistant's response content
    assistant_response = response.choices[0].message['content']
    print(assistant_response)
    return assistant_response