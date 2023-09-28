import codecs

flag = b"70" # 0x70
flag = codecs.decode(flag, encoding="hex")

print(flag)