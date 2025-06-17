import os
import tempfile
import whisperx
from moviepy import TextClip, CompositeVideoClip
import torch
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


def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"


def getCaptionsTimeStamped(clip):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        clip.audio.write_audiofile(temp_audio.name)
        temp_audio_path = temp_audio.name

    device = get_device()
    model = whisperx.load_model("large-v2", device=device)
    audio = whisperx.load_audio(temp_audio_path)
    result = model.transcribe(audio)

    # Load alignment model and align
    align_model, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result_aligned = whisperx.align(result["segments"], align_model, metadata, audio, device)

    os.remove(temp_audio_path)
    return result_aligned


def addCaptions(clip):
    subtitle_clips = []
    captions = getCaptionsTimeStamped(clip)
    for segment in captions["segments"]:
        txt = segment["text"].strip()
        txt_clip = TextClip(
            txt,
            fontsize=40,
            color='white',
            font='Arial',  # Make sure Arial is installed, or use another font
            size=(clip.w, 60),
            method='caption'
        ).set_duration(segment["end"] - segment["start"]) \
            .set_position(('center', 'bottom')) \
            .set_start(segment["start"])
        subtitle_clips.append(txt_clip)
    return CompositeVideoClip([clip, *subtitle_clips])


def main():
    return None


if __name__ == "__main__":
    main()

# TODO: fix this it generated brian for some reason
