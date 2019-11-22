def gen_auth_code(secret):
	import hmac
	import base64
	import struct
	import hashlib
	import time
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	try:
		key = base64.b32decode(secret)
	except:
		key = base64.b64decode(secret)
	h = hmac.new(key, struct.pack(">Q", int(time.time())//30), hashlib.sha1).digest()
	o = h[19] & 15
	h = str((struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000)
	return f"{h[:3]} {h[3:]}"

if __name__ == "__main__":
	print(gen_auth_code(input("Secret: ")))
