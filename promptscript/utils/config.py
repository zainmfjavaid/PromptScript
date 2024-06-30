
# For PromptScript CLI
COMMANDS = ['exit', 'save', 'show', 'chat', 'draw', 'listen', 'if', 'elif', 'else', 'for', 'while']

# For CommandExecutor and PersistentCommandExecutor
ILLEGAL_PARAMETER_NAMES = ['yield_output', 'get_environment_variable']

# Chat Defaults
DEFAULT_SYSTEM_PROMPT = 'you are a helpful chat assistant.'

# Models
## Contains list of supported models from different AI providers
## Occasionally contains mappings to simplify model usage (maps readable name to actual name). This is only done occasionally 
OPENAI_CHAT_MODELS = ['gpt-3.5-turbo', 'gpt-4-turbo', 'gpt-4-turbo-preview', 'gpt-4', 'gpt-4o']
OPENAI_IMAGE_MODELS = ['dall-e-3', 'dall-e-2']

ANTHROPIC_CHAT_MODELS = ['claude-3-5-sonnet-20240620', 'claude-3-opus-20240229', 'claude-3-sonnet-20240229', 'claude-3-haiku-20240307']
ANTHROPIC_CHAT_MAPPING = {'claude-3.5-sonnet': 'claude-3-5-sonnet-20240620', 'claude-3-5-sonnet': 'claude-3-5-sonnet-20240620',
                          'claude-3-opus': 'claude-3-opus-20240229', 'claude-3-sonnet': 'claude-3-sonnet-20240229',
                          'claude-3-haiku': 'claude-3-haiku-20240307'}

STABILITY_IMAGE_MODELS = ['ultra', 'core', 'sd3']