from PIL import Image
im = Image.open("style1.jpg")
print(im.format, im.size, im.mode)

# im.show()
im.save('style2.jpg', 'jpeg')