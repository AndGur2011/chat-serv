from PIL import Image
picture_ctk = Image.open("fish.jpg")
p = picture_ctk.rotate(90)
pi = picture_ctk.convert("L")
pi.show()