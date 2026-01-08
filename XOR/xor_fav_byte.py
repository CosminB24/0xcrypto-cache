from pwn import xor

#we have the initial hexadecimal string
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

#convert from hex to bytes:
bytes_string = bytes.fromhex(hex_string)
flag = ""

#iterate through all posibilites
for key in range(256):
    result = xor(bytes_string, key)
    try:
        #decode as ascii
        decoded = result.decode('ascii')
        #check for printable chars
        if all(32 <= ord(c) <= 126 for c in decoded):
            print(decoded)
            if 'crypto' in decoded:
               flag = decoded 
    except UnicodeDecodeError:
        #ignore errors
        continue

print("The flag is:", flag)
