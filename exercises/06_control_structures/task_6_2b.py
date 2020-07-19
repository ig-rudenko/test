# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP-адрес в формате 10.0.1.1: ")
while True:
    if len(ip.split('.')) == 4:
        for octet in ip.split('.'):
            if octet.isdigit() and 256 > int(octet) >= 0:
                pass
            else:
                break
        else:
            break
    print("Неправильный IP-адрес")
    ip = input("Введите IP-адрес в формате 10.0.1.1: ")
if int(ip.split('.')[0]) <= 223:
    print('unicast')
elif int(ip.split('.')[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

