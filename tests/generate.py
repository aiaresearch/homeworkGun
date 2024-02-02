from PIL import Image, ImageDraw, ImageFont
import random
import os

save_path = r"E:\homeworkGun\tests\images"

# Create a blank image
width, height = 200, 100

# Draw a number on the image
def generate_number_image():
    iter = int(input("Enter the number of iterations: "))

    for i in range(iter):
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 50)
        number_to_draw = str(random.randint(100000, 999999))
        text_width, text_height = draw.textsize(text=(number_to_draw), font=font)
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), number_to_draw, fill="black", font=font)
        output_path = os.path.join(save_path, str(number_to_draw) + ".png")
        image.save(output_path)