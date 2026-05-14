import ctypes

clibrary = ctypes.CDLL("/home/whoami/Python/Ctypes/clibrary.so")

#clibrary.display()

func = clibrary.display

func.argtypes = [ctypes.c_char_p, ctypes.c_int]
func.restype = ctypes.c_char_p

func(b"John", 2)
