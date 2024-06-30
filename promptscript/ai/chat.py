from typing import Dict, Any

from openai import OpenAI
from anthropic import Anthropic

from promptscript.utils.config import (
    DEFAULT_SYSTEM_PROMPT,
    OPENAI_CHAT_MODELS, 
    ANTHROPIC_CHAT_MODELS, 
    ANTHROPIC_CHAT_MAPPING
)


# Provider methods
def chat_openai(
    prompt: str,
    model: str, 
    api_key: str, 
    system_prompt: str=DEFAULT_SYSTEM_PROMPT, 
    **kwargs
) -> str:
    """Method for interacting with OpenAI chat models.

    Args:
        prompt (str): Prompt to send to LLM.
        model (str): What LLM to send the prompt to.
        api_key (str): OpenAI API key.
        system_prompt (str, optional): System instructions. Defaults to DEFAULT_SYSTEM_PROMPT.

    Returns:
        str: Chat response.
    """
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        **kwargs
    )
    return completion.choices[0].message.content

def chat_anthropic(
    prompt: str, 
    model: str, 
    api_key: str, 
    max_tokens: int=4096, 
    system_prompt: str=DEFAULT_SYSTEM_PROMPT,
    **kwargs
) -> str:
    """Method for interacting with Anthropic chat models.

    Args:
        prompt (str): Prompt to send to LLM.
        model (str): What LLM to send the prompt to.
        api_key (str): Anthropic API key.
        max_tokens (int, optional): Max response token length (required field for Anthropic API). Defaults to 4096.
        system_prompt (str, optional): System instructions. Defaults to DEFAULT_SYSTEM_PROMPT.

    Returns:
        str: Chat response.
    """
    client = Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[
            {'role': 'user', 'content': [{'type': 'text', 'text': prompt}]}
        ],
        **kwargs
    )
    return message.content[0].text

# Router
def _construct_kwargs(**kwargs) -> Dict[str, Any]:
    """Helper method for constructing kwargs. Only adds a value if its value is non-null.

    Returns:
        Dict[str, Any]: Dictionary of kwargs.
    """
    return {key: value for key, value in kwargs.items() if value is not None}

def route_chat(
    prompt: str, 
    model: str, 
    api_key: str,
    max_tokens: int=None,
    system_prompt: str=None
) -> str:
    """Routes request to provider methods based on model name.

    Args:
        prompt (str): Prompt to send to LLM.
        model (str): What LLM to send the prompt to.
        api_key (str): The API key for whatever service the chat is getting sent to.
        max_tokens (int, optional): Max response token length. Defaults to None.
        system_prompt (str, optional): System instructions. Defaults to None.

    Raises:
        Exception: If an invalid chat model is provided.

    Returns:
        str: Chat response.
    """
    model = model.lower()
    kwargs = _construct_kwargs(max_tokens=max_tokens, system_prompt=system_prompt)
    
    if model in OPENAI_CHAT_MODELS:
        return chat_openai(prompt, model, api_key, **kwargs)
    
    elif model in ANTHROPIC_CHAT_MODELS or model in ANTHROPIC_CHAT_MAPPING:
        model = ANTHROPIC_CHAT_MAPPING.get(model, model)
        return chat_anthropic(prompt, model, api_key, **kwargs)
    
    raise Exception('ERROR: Invalid chat model')