# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = "192.168.3.1"
print("Network:\n{0:<8}  {1:<8}  {2:<8}  {3:<8}\n{0:08b}  {1:08b}  {2:08b}  {3:08b}\n".format(
int(ip.split('.')[0]), int(ip.split('.')[1]), int(ip.split('.')[2]), int(ip.split('.')[3])))

