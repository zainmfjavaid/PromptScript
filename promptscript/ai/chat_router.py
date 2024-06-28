from openai import OpenAI
from promptscript.utils.config import OPENAI_CHAT_MODELS
        

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
    if model.lower() in OPENAI_CHAT_MODELS:
        return chat_openai(prompt, model, api_key)
    raise Exception('ERROR: Invalid chat model')