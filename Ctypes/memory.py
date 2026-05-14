import ctypes

clibrary = ctypes.CDLL("/home/whoami/Python/Ctypes/clibrary.so")

string = ctypes.create_string_buffer(100)
string.value = b"Hello world"

print(string)

string.value = b"Goodby world"

print(string)
