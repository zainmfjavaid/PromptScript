from openai import OpenAI
        

def chat_openai(api_key: str, prompt: str, model: str) -> str:
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'you are a helpful chat assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return completion.choices[0].message.content

def route_chat(api_key: str, prompt: str, model: str) -> str:
    if model.lower().startswith('gpt'):
        return chat_openai(api_key, prompt, model)
    raise Exception('ERROR: Invalid chat model')