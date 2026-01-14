def read_image(path):
    if not path:
        raise ValueError("Image path is empty")
    print(f"Reading image from {path}")
    return path

def convert_to_grayscale(img):
    if img is None:
        raise ValueError("No image provided")
    print("Converting image to grayscale")
    return "grayscale_image"

def show_image(img):
    if img is None:
        print("Nothing to display")
        return
    print(f"Displaying {img}")

def save_image(img, path):
    print(f"Saving image to {path}")