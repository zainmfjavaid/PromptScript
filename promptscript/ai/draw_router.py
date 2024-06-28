import base64
from openai import OpenAI
from promptscript.utils.config import OPENAI_IMAGE_MODELS


def draw_dalle(prompt: str, model: str, api_key: str, response_format: str) -> str:
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
        response_format=response_format
    )
    return response.data[0]

def route_draw(prompt: str, model: str, api_key: str, destination_file: str=None) -> str:
    if model.lower() in OPENAI_IMAGE_MODELS:
        if destination_file:
            b64 = draw_dalle(prompt, model, api_key, 'b64_json').b64_json
            with open(destination_file, 'wb') as f:
                f.write(base64.b64decode(b64))
            return
        else:
            return draw_dalle(prompt, model, api_key, 'url').url
    raise Exception(f'ERROR: Invalid draw model')