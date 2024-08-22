import base64

file_to_be_send = "README.md"
audio_raw = b''
with open(file_to_be_send, 'rb') as fd:
    audio_raw = fd.read()
# print(audio_raw)
audio_raw_str = base64.b64encode(audio_raw).decode('utf-8')
# print(audio_raw_str)

# 网络传输.....

file_receive_name = file_to_be_send + ".back_up"
audio_raw_decode = base64.b64decode(audio_raw_str)
# print(audio_raw_decode)
with open(file_receive_name, 'wb') as fd:
    fd.write(audio_raw_decode)
