import os
import tempfile

from moviepy import Clip, AudioFileClip
from pydub import AudioSegment
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from resources import Conversation, Dialogue


def getVoice(characterName):
    voices = {
        "peter": ("1oDyQNcCOcFys29zvXRv", "eleven_multilingual_v2"),
        "stewie": ("3corgaVLrsFZyd9HC4Vy", "eleven_multilingual_v2"),
    }
    return voices.get(characterName.lstrip().split(" ")[0].lower(), None)


def getAudioClip(characterName, text):
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY")
    )
    voiceMeta = getVoice(characterName)
    audio_bytes = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id=voiceMeta[0],
        model_id=voiceMeta[1],
        output_format="mp3_44100_128",
    )
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        for chunk in audio_bytes:
            temp_file.write(chunk)
        temp_file_path = temp_file.name

    segment = AudioSegment.from_file(temp_file_path, format="mp3")
    os.unlink(temp_file_path)
    return segment


def getAudio(script: Conversation, path: str = None):
    audio_segments = []
    for dialogue in script.dialogue:
        characterName = dialogue.character
        text = dialogue.text
        if not getVoice(characterName):
            print(f"Error: No voice found for {characterName}.")
            continue
        segment = getAudioClip(characterName, text)
        if not segment:
            print(f"Error: No audio generated for {characterName} with text: {text}")
            continue
        audio_segments.append(segment)
    if audio_segments:
        final_audio = sum(audio_segments)
        if path:
            final_audio.export(path, format="wav")
            return path
        else:
            temp_out = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            final_audio.export(temp_out.name, format="wav")
            return temp_out.name
    return None


def getLength(path: str):
    if not os.path.exists(path):
        print(f"Error: File {path} does not exist.")
        return 0
    audio = AudioSegment.from_file(path)
    return len(audio) / 1000  # Return length in seconds


def addAudio(audio_path: str, video_clip: Clip):
    if not os.path.exists(audio_path):
        print(f"Error: Audio file {audio_path} does not exist.")
        return video_clip
    audio_clip = AudioFileClip(audio_path)
    return video_clip.with_audio(audio_clip)


def example():
    # Example usage
    example_script = Conversation(dialogue=[
        Dialogue(character="Peter", text="Hey Stewie, did you know about the PGC-1α signaling cascade?"),
        Dialogue(character="Stewie",
                 text="Oh, you mean the endurance-induced transcription factors that expand mitochondrial content? Fascinating!"),
        Dialogue(character="Peter",
                 text="Exactly! And how leucine binds to Sestrin2 to activate mTOR is just mind-blowing."),
    ])
    audio_file = getAudio(example_script)
    if audio_file:
        print(f"Audio generated successfully: {audio_file}")
    else:
        print("Failed to generate audio.")


if __name__ == "__main__":
    example()
