import re 
from binascii import unhexlify

def xorstr(str1, str2):
	return [char1^char2 for char1, char2 in zip(str1, str2)]

ct = unhexlify(b"1b591484db962f7782d1410afa4a388f7930067bcef6df546a57d9f873")
key = [88,17,64,198,160,251,74,26,178,163,56,85,137,126,94,188,38,83,116,2,190,130,239,11,12,99,232,148,14,107,27,194,98,21,224,135,61,173,116,148,78,124,152,228,207,8,46,78,193,79,116,202,239,198,46,213,233,92,108,151,207,246,177,172]

print("".join([chr(char) for char in xorstr(ct, key)]))
