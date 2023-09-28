# 01100110 01100001 01101100 01100011 01101111 01101110

x1 = b"01100011"
x2 = b"01101000"
x3 = b"01100001"
x4 = b"01101001"
x5 = b"01110010"


x1 = int(x1, 2)
x2 = int(x2, 2)
x3 = int(x3, 2)
x4 = int(x4, 2)
x5 = int(x5, 2)

print(chr(x1))
print(chr(x2))
print(chr(x3))
print(chr(x4))
print(chr(x5))


decimal = "143 157 155 160 165 164 145 162".split(" ")
result = ""
for x in decimal:
    result += chr(int(x, 8))
print(result)


x = b"616e696d6174696f6e"
import _codecs
result = _codecs.decode(x, encoding="hex")
print(result)

