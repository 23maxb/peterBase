import os


def convertImageToPNG(path: os.PathLike):


def processImages(path: os.PathLike):
    print("Processing images in ", path)
    from PIL import Image
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                img = Image.open(file)
                new_path = os.path.splitext(file)[0] + '.png'
                img.save(new_path, 'PNG')
                print(f"Converted {file} to {new_path}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
                pass


def addImages(script, clip):
    return clip


if __name__ == "__main__":
    print("dodo")
