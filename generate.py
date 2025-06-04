from idna.idnadata import scripts
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from numpy.f2py.f2py2e import CombineIncludePaths
from numpy.ma.core import true_divide

from parkour import parkour
from parkour.parkour import getParkour
from audio.getAudio import getAudio, getLength, addAudio
from text.getText import getScript, addCaptions
from images.getImage import addImages

from dotenv import load_dotenv


def main():
    load_dotenv()
    desiredLength = 1  # length in min
    subject = "bench press"
    characters = ["Peter", "Stewie"]
    speakerTimeStamps = {"": ""}

    script = getScript(subject, characters)
    audio = getAudio(script)
    TRUE_LENGTH = getLength(audio)
    toReturn = getParkour(TRUE_LENGTH * 1.0)

    toReturn = addAudio(audio, toReturn)
    toReturn = addCaptions(script, toReturn)
    toReturn = addImages(script, toReturn)


if __name__ == "__main__":
    # load_dotenv()
    audio = "tempfile.wav"
    TRUE_LENGTH = getLength(audio)
    toReturn = getParkour(TRUE_LENGTH)
    toReturn = addAudio(audio, toReturn)
    print("hi")
    toReturn = addCaptions(toReturn)
    toReturn.write_videofile("output.mp4")
