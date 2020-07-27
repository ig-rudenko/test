# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    with open(config_filename, 'r') as config:
        access = {}
        trunk = {}
        interface = ''
        for line in config:
            if 'interface ' in line and not 'lan' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access[interface] = int(vlan)
                interface = ''
            elif 'trunk allowed vlan' in line:
                trunk_vlans = line.split()[-1]
                trunk[interface] = [int(num) for num in trunk_vlans.split(',')]
                interface = ''
            elif "!" in line and interface:
                access[interface] = 1
                interface = ''
    result = (access, trunk)
    print(result)
    return result


get_int_vlan_map('config_sw2.txt')

