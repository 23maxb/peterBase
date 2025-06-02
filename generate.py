from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from parkour import parkour
from parkour.parkour import getParkour

if __name__ == "__main__":
    clipLength = 1  # length in min
    toReturn = getParkour(clipLength * 1.0)
    
