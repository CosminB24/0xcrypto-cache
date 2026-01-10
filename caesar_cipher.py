TEXT = "PUXKN QJRA ANLNREN TRWPMXV"

for shift in range(26):
    result = ""
    for char in TEXT:
        if "A" <= char <= "Z":
            result += chr((ord(char) - ord('A') + shift) % 26 + ord("A"))
        else:
            result += char
    print(result)