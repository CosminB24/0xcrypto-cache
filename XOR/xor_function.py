#Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
from pwn import *

text = "label"
number = 13

print(xor(text, number))