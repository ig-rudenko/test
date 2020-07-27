# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)

def convert_config_to_dict(config_filename):
    with open(config_filename, 'r') as conf:
        config = {}
        key = ''
        values = []
        for line in conf:
            if not ignore_command(line, ignore) and not "!" in line:
                if not line.startswith(' '):            # Если находим ключ, то...
                    if key:                                 # Если ключ уже был, то...
                        config[key] = values                    # ...записываем старый ключ
                        values, key = [], ''                    # очищаем значения key и value.
                    key = line.strip()                      # ...указываем ключ
                    print("key: "+key.strip())              # выводим ключ.
                elif key:                               # Иначе, Если ключ найден, то...
                    if not values:                          # Если это первое значение, то...
                        values = [line.strip()]                 # ...создаем список из одного элемента.
                        print('первый: ')
                    else:                                   # Иначе...
                        values = values.append(line.strip())    # ...добавляем значение в список.
                    print(values)
                    print("value: "+line.strip())
        print(config)

convert_config_to_dict("config_sw1.txt")

