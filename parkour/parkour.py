from moviepy import VideoFileClip
from moviepy.video.fx.Crop import Crop
import random


def getParkour(lengthOfClip):
    start = random.randint(0, 199 - lengthOfClip)
    clip = (
        VideoFileClip("resources/MC Parkour.mp4")
        .subclipped(start, start + lengthOfClip)
        .without_audio()
    )

    # Get original dimensions
    w, h = clip.size

    # Create and apply crop effect
    crop_effect = Crop(
        x_center=w / 2,
        y_center=h / 2,
        width=(1080 / 1920) * h,
        height=h
    )
    print((1080 / 1920) * h)

    clip = crop_effect.apply(clip)

    return clip


if __name__ == "__main__":
    print("temp")
    a = getParkour(4)
    a.write_videofile("parkour_test.mp4")
    print("done")
