from openai import OpenAI


def draw_dalle(api_key: str, prompt: str, model: str) -> str:
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1
    )
    return response.data[0].url

def route_draw(api_key: str, prompt: str, model: str) -> str:
    if model.lower() in ['dall-e-3', 'dall-e-2']:
        return draw_dalle(api_key, prompt, model)
    raise Exception(f'ERROR: Invalid draw model ([dall-e-3, dall-e-2])')