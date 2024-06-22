from openai import OpenAI
        

def chat_openai(prompt: str, model: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'you are a helpful chat assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return completion.choices[0].message.content

def route_chat(prompt: str, model: str, api_key: str) -> str:
    if model.lower().startswith('gpt'):
        return chat_openai(prompt, model, api_key)
    raise Exception('ERROR: Invalid chat model')