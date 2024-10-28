from PIL import Image

image = Image.open("images/example.jpg")
rotated_image = image.rotate(45)
rotated_image.save("images/rotated.jpg")
# rotated_image.save("images\rotated.jpg", format="JPEG")