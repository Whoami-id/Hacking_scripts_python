import ctypes

clibrary = ctypes.CDLL("/home/whoami/Python/Ctypes/clibrary.so")


num = ctypes.c_int(100)
ptr = ctypes.pointer(num)
print(ptr.contents)


ptr2 = ctypes.POINTER(ctypes.c_int)
ptr2.contents = num
print(ptr.contents)