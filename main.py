from PIL import Image

image = Image.open("images/example.jpg")
rotated_image = image.rotate(45)
rotated_image.save("images/rotated.jpg")
width = image.width
height = image.height
cmyk_image = image.convert("CMYK")
color_model = cmyk_image.mode

print("""\
      Ширина - {width}
      Высота - {height}
      Цветовая модель — {color_model} """.format(width=width, height=height, color_model=color_model))
