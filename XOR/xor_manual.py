#Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
text = input("Choose a word for XOR: ")
number = int(input("Choose a number: "))

print("crypto={", end="")
for char in text:
    text_xor = chr(ord(char) ^ number)
    print(text_xor, end="")

print("}", end="")