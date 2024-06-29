from openai import OpenAI
from anthropic import Anthropic
from promptscript.utils.config import (
    OPENAI_CHAT_MODELS, 
    ANTHROPIC_CHAT_MODELS, 
    ANTHROPIC_CHAT_MAPPING
)


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

def chat_anthropic(prompt: str, model: str, api_key: str) -> str:
    client = Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        system='you are a helpful chat assistant.',
        messages=[
            {'role': 'user', 'content': [{'type': 'text', 'text': prompt}]}
        ]
    )
    return message.content[0].text

def route_chat(prompt: str, model: str, api_key: str) -> str:
    model = model.lower()
    
    if model in OPENAI_CHAT_MODELS:
        return chat_openai(prompt, model, api_key)
    
    elif model in ANTHROPIC_CHAT_MODELS or model in ANTHROPIC_CHAT_MAPPING:
        model = ANTHROPIC_CHAT_MAPPING.get(model, model)
        return chat_anthropic(prompt, model, api_key)
    
    raise Exception('ERROR: Invalid chat model')