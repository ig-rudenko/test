#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip, mask = argv[1], argv[2]
m = str('1'*int(mask)+'0'*(32-int(mask)))
ip11, ip22, ip33, ip44 = str(bin(int(ip.split('.')[0])))[2:], str(bin(int(ip.split('.')[1])))[2:], \
                         str(bin(int(ip.split('.')[2])))[2:], str(bin(int(ip.split('.')[3])))[2:]
ip1, ip2, ip3, ip4 = '0'*(8-len(ip11))+ip11, '0'*(8-len(ip22))+ip22, '0'*(8-len(ip33))+ip33, '0'*(8-len(ip44))+ip44

IP1, IP2, IP3, IP4 = ip1[0:m[0:8].count('1')]+'0'*(8-len(ip1[0:m[0:8].count('1')])),\
                     ip2[0:m[8:16].count('1')]+'0'*(8-len(ip1[0:m[8:16].count('1')])), \
                     ip3[0:m[16:24].count('1')]+'0'*(8-len(ip1[0:m[16:24].count('1')])),\
                     ip4[0:m[24:32].count('1')]+'0'*(8-len(ip1[0:m[24:32].count('1')]))
print(IP1, IP2, IP3, IP4)
print("Network:\n{:<8} {:<8} {:<8} {:<8}\n{:8} {:8} {:8} {:8}\n".format(
    int(IP1, 2), int(IP2, 2), int(IP3, 2), int(IP4, 2), IP1, IP2, IP3, IP4),
    "Mask:\n/{:}\n{:<8} {:<8} {:<8} {:<8}\n{:<08} {:<08} {:<08} {:<08}".format(
        mask, int(m[0:8], 2), int(m[8:16], 2), int(m[16:24], 2), int(m[24:32], 2),
        int(m[0:8]), int(m[8:16]), int(m[16:24]), int(m[24:32])))

