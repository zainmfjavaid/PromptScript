import base64
import requests
from openai import OpenAI
from promptscript.utils.config import (
    OPENAI_IMAGE_MODELS,
    STABILITY_IMAGE_MODELS
)


def save_to_file(func):
    def wrapper(prompt: str, model: str, api_key: str, destination_file: str) -> None:
        b64 = func(prompt, model, api_key)
        with open(destination_file, 'wb') as f:
            f.write(base64.b64decode(b64))
    return wrapper

# Provider methods
@save_to_file
def draw_dalle(prompt: str, model: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
        response_format='b64_json'
    )
    return response.data[0].b64_json

@save_to_file
def draw_stability(prompt: str, model: str, api_key: str) -> str:
    url = f'https://api.stability.ai/v2beta/stable-image/generate/{model}'
    headers = {'Accept': 'application/json', 'Authorization': f'Bearer {api_key}'}
    params = {'prompt': prompt}
    files = {'none': ''}
    
    response = requests.post(url, headers=headers, data=params, files=files).json()
    if 'image' in response:
        return response['image']
    return Exception(f"Error: {response['errors']}")
    
# Router
def route_draw(prompt: str, model: str, api_key: str, destination_file: str) -> None:
    model = model.lower()
    
    if model in OPENAI_IMAGE_MODELS:
        draw_dalle(prompt, model, api_key, destination_file)
        return
    
    elif model in STABILITY_IMAGE_MODELS:
        b64 = draw_stability(prompt, model, api_key, destination_file)
        return
    
    raise Exception(f'ERROR: Invalid draw model')