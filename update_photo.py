from PIL import Image
import random

# Open the original photo.png image
original_image = Image.open("photo.png")

x = random.randint(1,3)
if x == 1:
    new_image = Image.open("0.png")
elif x == 2:
    new_image = Image.open("1.png")
else:
    new_image = Image.open("7.png")

# Replace the original image with the new image
original_image.paste(new_image)

# Save the updated image as photo.png
original_image.save("photo.png")

print("Successfully updated photo.png with new.png")
