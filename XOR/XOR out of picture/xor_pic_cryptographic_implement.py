import numpy as np
from PIL import Image
from pwn import *

#convert both pics to rgb
pic1 = np.array(Image.open("flag_7ae18c704272532658c10b5faad06d74.png").convert("RGB"))
pic2 = np.array(Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png").convert("RGB"))

#XOR between the two rgb arrays
flag = np.bitwise_xor(pic1, pic2)
#king julian is now even clear
Image.fromarray(flag).show()