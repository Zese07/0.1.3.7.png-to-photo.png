from PIL import Image
import random


image_files = ['0.png', '1.png', '3.png', '7.png']
new_image_filename = random.choice(image_files)
new_image = Image.open(new_image_filename)

photo = Image.open('photo.png')
photo = new_image.copy()
photo.save('photo.png')
