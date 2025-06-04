import os
import tempfile
import whisperx
from moviepy import TextClip, CompositeVideoClip

from resources import getFitnessPrompt, getTopics, Conversation
from dotenv import load_dotenv
from openai import OpenAI


def getText(subject, characters=None, api_key=None):
    # load api key
    if api_key is None:
        api_key = os.getenv('OPENAI_API_KEY')  # Get API key from environment
    client = OpenAI(api_key=api_key)

    completion = client.responses.parse(
        model="gpt-4.1-mini-2025-04-14",
        input=[
            {
                "role": "system", "content": "You are a helpful writer. Writing scripts for short videos."
            },
            {
                "role": "user", "content": getFitnessPrompt(subject, characters, getTopics()[1])
            },
        ],
        text_format=Conversation,
    )
    print(completion)
    return completion.output_parsed


def getScript(subject, characters):
    getText(subject, characters)
    return "hi"


def getCaptionsTimeStamped(clip):
    # Export audio from the video clip to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        clip.audio.write_audiofile(temp_audio.name)
        temp_audio_path = temp_audio.name

    # Load whisperx model
    model = whisperx.load_model("base", device="cpu")
    audio = whisperx.load_audio(temp_audio_path)
    result = model.transcribe(audio)

    # Clean up temp file
    os.remove(temp_audio_path)

    return result['segments']  # Each segment contains 'start', 'end', 'text'


def addCaptions(clip):
    subtitle_clips = []
    captions = getCaptionsTimeStamped(clip)
    for segment in captions["segments"]:
        txt = segment["text"]
        txt_clip = TextClip(
            text=txt,
            font_size=40,
            color='white',
            size=(clip.w, 60)
        ).with_duration(segment["end"] - segment["start"]).with_position(('center', 'center')).with_start(
            segment["start"])
        subtitle_clips.append(txt_clip)
    return CompositeVideoClip([clip, *subtitle_clips])  # star unpacks iterable 


def main():
    return None


if __name__ == "__main__":
    main()

# TODO: fix this it generated brian for some reason
