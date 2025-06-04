import math

from moviepy import VideoFileClip
from moviepy.video.fx.Crop import Crop
import random
import os


def getParkour(lengthOfClip):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_dir, "resources", "MC Parkour.mp4")
    start = random.randint(0, 199 - math.floor(lengthOfClip))
    clip = (
        VideoFileClip(video_path)
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
