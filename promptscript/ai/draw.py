import base64
import requests
from typing import Callable

from openai import OpenAI

from promptscript.utils.config import (
    OPENAI_IMAGE_MODELS,
    STABILITY_IMAGE_MODELS
)


def save_to_file(func: Callable) -> Callable:
    """Decorator to save base64-encoded data to a file.

    Args:
        func (Callable): Function to wrap.
        
    Returns:
        Callable: Wrapped function.
    """
    def wrapper(
        prompt: str,
        model: str, 
        api_key: str,
        destination_file: str
    ) -> None:
        """Wrapper function that saves generated image to a file.

        Args:
            prompt (str): Prompt to generate image based on.
            model (str): The model to use for image generation.
            api_key (str): API key for the image generation service.
            destination_file (str): File path to save generated image to.
        """
        b64 = func(prompt, model, api_key)
        with open(destination_file, 'wb') as f:
            f.write(base64.b64decode(b64))
    return wrapper

# Provider methods
@save_to_file
def draw_dalle(
    prompt: str, 
    model: str, 
    api_key: str
) -> str:
    """Method for interacting with OpenAI image generation.

    Args:
        prompt (str): Prompt to generate image based on.
        model (str): The model to use for image generation.
        api_key (str): OpenAI API key.

    Returns:
        str: base64-encoded image data.
    """
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
def draw_stability(
    prompt: str, 
    model: str, 
    api_key: str
) -> str:
    """Method for interacting with StabilityAI image generation.

    Args:
        prompt (str): Prompt to generate image based on.
        model (str): The model to use for image generation.
        api_key (str): Stability API key.

    Returns:
        str: base64-encoded image data.
    """
    url = f'https://api.stability.ai/v2beta/stable-image/generate/{model}'
    headers = {'Accept': 'application/json', 'Authorization': f'Bearer {api_key}'}
    params = {'prompt': prompt}
    files = {'none': ''}
    
    response = requests.post(url, headers=headers, data=params, files=files).json()
    if 'image' in response:
        return response['image']
    return Exception(f"Error: {response['errors']}")
    
# Router
def route_draw(
    prompt: str, 
    model: str, 
    api_key: str, 
    destination_file: str
) -> None:
    """Routes request to provider methods based on model name.

    Args:
        prompt (str): Prompt to generate image based on.
        model (str): The model to use for image generation.
        api_key (str): API key for the image generation service.
        destination_file (str): File path to save generated image to.

    Raises:
        Exception: If an invalid image generation model is provided.
    """
    model = model.lower()
    
    if model in OPENAI_IMAGE_MODELS:
        draw_dalle(prompt, model, api_key, destination_file)
        return
    
    elif model in STABILITY_IMAGE_MODELS:
        b64 = draw_stability(prompt, model, api_key, destination_file)
        return
    
    raise Exception(f'ERROR: Invalid draw model')