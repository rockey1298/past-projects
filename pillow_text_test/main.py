import PIL
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw


#  this is how you would import a file using pillow and displaying the image
file = "mit-mosin.png"
mit_group = Image.open(file)
# mit_group.show()

mit_group = mit_group.convert("RGB")

# draw = ImageDraw.Draw(mit_group)

r, g, b = mit_group.split()
print(r, g, b)


# draw.text((0, 0), "Hello world!", features="Box")

# draw.rectangle((0, 0), fill="WHITE", width=1)
# mit_group.show()
# help(PIL.ImageFilter)

# help(draw)
