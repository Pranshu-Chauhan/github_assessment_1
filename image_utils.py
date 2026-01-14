def read_image(path):
    if not path:
        raise ValueError("Image path is empty")
    print(f"Reading image from {path}")
    return path

def convert_to_grayscale(img):
    print("Converting image to grayscale")

def show_image(img):
    print("Showing image")

def save_image(img, path):
    print(f"Saving image to {path}")