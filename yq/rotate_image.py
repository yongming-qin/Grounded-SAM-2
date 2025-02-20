import os
from PIL import Image
import sys

def rotate_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            rotated_img = img.rotate(180, expand=True)
            rotated_img.save(os.path.join(output_folder, filename))
            print(f"Rotated and saved: {os.path.join(output_folder, filename)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rotate_image.py <input_folder>")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_folder = os.path.join(os.path.dirname(os.path.dirname(input_folder)), 'rotated_images')
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    rotate_images(input_folder, output_folder)