import codecs

flag = b"cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" # byte object
flag = codecs.decode(flag, encoding="base64")
print(flag)