from PIL import Image

# Open the original photo.png image
original_image = Image.open("photo.png")

# Open the new.png image
new_image = Image.open("new.png")

# Replace the original image with the new image
original_image.paste(new_image)

# Save the updated image as photo.png
original_image.save("photo.png")

print("Successfully updated photo.png with new.png")
