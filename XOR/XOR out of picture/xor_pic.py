#I've hidden two cool images by XOR with the same secret key so you can't see them!
from PIL import Image, ImageChops

#open 1st & 2nd pic
pic1 = Image.open("flag_7ae18c704272532658c10b5faad06d74.png")
pic2 = Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png")

#gets the different bits from the pictures
flag = ImageChops.difference(pic1, pic2)
#it's king julian!!
flag.show()