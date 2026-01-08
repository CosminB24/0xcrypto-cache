from pwn import xor

#the encrypted message in hex
hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

#from hex to bytes
bytes_string = bytes.fromhex(hex_string)
key = b'crypto{'

#using a key to decrypt the message and decoding in utf-8 format
decrypt = xor(bytes_string, key).decode("utf-8")
print(decrypt)

#decrypt the message with the key found in previous message
secret_key = b'myXORkey'
flag = xor(bytes_string, secret_key)
print(flag)
