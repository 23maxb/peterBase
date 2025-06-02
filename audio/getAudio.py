import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

if __name__ == "__main__":


def getAudioClip(characterName, text):
    load_dotenv()
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY")
    )
    voiceMeta = getVoice(characterName)
    audio = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id=voiceMeta[0],
        model_id=voiceMeta[1],
        output_format="mp3_44100_128",
    )


def getVoice(characterName):
    """
    Get the voice ID for a given character name.
    Args:
        characterName (str): The name of the character.
    Returns:
        (str, str): A tuple containing the voice ID and model ID.
    """
    voices = {
        "Peter": ("1oDyQNcCOcFys29zvXRv", "eleven_multilingual_v2"),
        "Stewie": ("3corgaVLrsFZyd9HC4Vy", "eleven_multilingual_v2"),
    }
    return voices.get(characterName, None)  # Return None if character not found
