from PIL import Image

image = Image.open("images/monro.jpg")
red, green, blue = image.split()
cut_left = 50   #   only an even number
cut_middle = cut_left/2
transparency = 0.3

cut_left_red = (cut_left, 0, image.width, image.height)
cropped_left_red = red.crop(cut_left_red)
cut_middle_red = (cut_middle, 0, image.width-cut_middle, image.height)
cropped_middle_red = red.crop(cut_middle_red)
mixing_red = Image.blend(cropped_left_red, cropped_middle_red, transparency)

cut_right_blue = (0, 0, image.width-cut_left, image.height)
cropped_right_blue = blue.crop(cut_right_blue)
cut_middle_blue = (cut_middle, 0, image.width-cut_middle, image.height)
cropped_middle_blue = blue.crop(cut_middle_blue)
mixing_blue = Image.blend(cropped_right_blue, cropped_middle_blue, transparency)

cut_middle_green = (cut_middle, 0, image.width-cut_middle, image.height)
cropped_middle_green = green.crop(cut_middle_green)

new_image = Image.merge("RGB", (mixing_red, cropped_middle_green, mixing_blue))
new_image.save("images/mixing_monro.jpg")
new_image.thumbnail((80, 80))
new_image.save("images/avatar.jpg")

