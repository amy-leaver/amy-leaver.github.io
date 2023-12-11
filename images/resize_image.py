from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    image = Image.open(input_path)
    resized_image = image.resize((new_width, new_height))
    resized_image.save(output_path)

if __name__ == "__main__":
    input_image_path = "your_image.jpg"  # Replace with the actual image file name
    output_image_path = "resized_image.jpg"  # Replace with the desired output file name
    new_width = 800  # Replace with the desired width
    new_height = 600  # Replace with the desired height

    resize_image(input_image_path, output_image_path, new_width, new_height)
