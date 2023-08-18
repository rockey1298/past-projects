import PIL
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


# # image file
# file = "mit-mosin.png"
# # mit group image open
# mit_group = Image.open(file)

# images = []


# # help(PIL)
# # dir(PIL)
# # help(Image.open)
# print(mit_group)
# # mit_group.show()
# # you need to urn this to be able to use the image object with other functions provided by pillow
# mit_group = mit_group.convert("RGB")
# # blurred_image = mit_group.filter(PIL.ImageFilter.BLUR)
# # blurred_image.show()
# enhancer = ImageEnhance.Brightness(mit_group)
# for i in range(0, 10):
#     images.append(enhancer.enhance(i / 10))
# # print(images)

# first_image = images[0]
# # this is creating a canvas for us to put the rest of the images on! we are making ti 10 images tall,
# contact_sheet = PIL.Image.new(
#     first_image.mode, (first_image.width, 10 * first_image.height)
# )

# current_location = 0
# for img in images:
#     contact_sheet.paste(mit_group, (0, current_location))
#     current_location = current_location + 450

# contact_sheet = contact_sheet.resize((160, 900))
# contact_sheet.show()
# # help(ImageEnhance._Enhance)


# read image and convert to RGB
image = Image.open("mit-mosin.png")
image = image.convert("RGB")

# build a list of 9 images which have different brightnesses
enhancer = ImageEnhance.Brightness(image)
images = []
for i in range(1, 10):
    images.append(enhancer.enhance(i / 10))

# create a contact sheet from different brightnesses
first_image = images[0]
contact_sheet = PIL.Image.new(
    first_image.mode, (first_image.width * 3, first_image.height * 3)
)
x = 0
y = 0

# why dont we just hardcode the rows for each color to a list to make things easier?
red_pictures = images[0:3]
green_pictures = images[3:6]
blue_pictures = images[6:9]

my_contact_sheet = PIL.Image.new(
    first_image.mode, (first_image.width * 3, first_image.height * 3)
)
print(red_pictures)
# first row of pictures
for red in red_pictures:
    my_contact_sheet.paste(red, (x, y))
    x = x + red.width
# setting the hieght for next row

y = y + first_image.height
x = 0

# second row of pictures

for green in green_pictures:

    my_contact_sheet.paste(green, (x, y))
    x = x + first_image.width

# this is how your setting the height and width for the rows.
y = y + first_image.height
x = 0

# third row of pictures

for blue in blue_pictures:

    my_contact_sheet.paste(blue, (x, y))
    x = x + blue.width
my_contact_sheet.show()

# for img in images:
#     # Lets paste the current image into the contact sheet
#     contact_sheet.paste(img, (x, y))
#     # Now we update our X position. If it is going to be the width of the image, then we set it to 0
#     # and update Y as well to point to the next "line" of the contact sheet.
#     if x + first_image.width == contact_sheet.width:
#         x = 0
#         y = y + first_image.height
#     else:
#         x = x + first_image.width

# # resize and display the contact sheet
# contact_sheet = contact_sheet.resize(
#     (int(contact_sheet.width / 2), int(contact_sheet.height / 2))
# )
# contact_sheet.show()
