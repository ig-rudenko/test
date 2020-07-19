# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
access = access_template[0]+'\n'+access_template[1]+'\n'+access_template[2]+'\n'+access_template[3]+'\n'+access_template[4]
trunk = trunk_template[0]+'\n'+trunk_template[1]+'\n'+trunk_template[2]
dic = {'access': access, 'trunk': trunk}
vlan = {'access': 'номер VLAN: ', 'trunk': 'разрешенные VLANы: '}
interface = input("Введите режим работы интерфейса (access/trunk): ")
int_num = input("Введите тип и номер интерфейса: ")
vlan_num = input(f"Введите {vlan[interface]}")
print(f"interface {int_num}\n{str(dic[interface]).format(vlan_num)}")

