import base64

# base64 转码
message = "plain message"


the_bytes = bytes(message, "utf-8")
a = base64.b64encode(the_bytes)
c = base64.b64encode(the_bytes).decode('utf-8')
print("Encoding:", a)
print("Encoding:", c)

b = base64.b64decode(a).decode("utf-8")
print("Decoding:", b)
d = base64.b64decode(c).decode("utf-8")
print("Decoding:", d)