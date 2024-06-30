from openai import OpenAI


# Provider methods
def listen_openai(
    audio_file_path: str, 
    api_key: str
) -> str:
    """Method for interacting with OpenAI Whisper.

    Args:
        audio_file_path (str): File to transcribe.
        api_key (str): OpenAI API key.

    Returns:
        str: Transcribed text.
    """
    client = OpenAI(api_key=api_key)
    audio_file = open(audio_file_path, 'rb')
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
        response_format='text'
    )
    return transcription

# Router
def route_listen(
    audio_file_path: str, 
    api_key: str
) -> str:
    """Routes request to provider methods based on model name (currently only routes to OpenAI).

    Args:
        audio_file_path (str): File to transcribe.
        api_key (str): Transcription service API key.

    Returns:
        str: Transcribed text.
    """
    return listen_openai(audio_file_path, api_key)