# picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}

import codecs

flag = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 97, 102, 100, 53, 102, 100, 97, 52, 125, 10]

result = ""

for x in flag:
    result += chr(x)

print(result)

