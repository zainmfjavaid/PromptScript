from openai import OpenAI


# Provider methods
def listen_openai(audio_file_path: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)
    audio_file = open(audio_file_path, 'rb')
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
        response_format='text'
    )
    return transcription

# Router
def route_listen(audio_file_path: str, api_key: str) -> str:
    return listen_openai(audio_file_path, api_key)