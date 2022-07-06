"""JavaScript Object Notation - JSON"""
# Единый формат хранения и передачи данных между компьютерами, сервисами, 
# приложениями и языками программирования через сеть Интернет.
# <filename>.json

# {
#     "id": 1,
#     "author": "John",
#     "posts": []
# } --- Это JSON, задача научиться переводить JSON в Python Dict

# !!!
# JS object == {}
# PY dict == {}
# JSON == {}

# """Процессы Сериализации данных и их Десериализации"""

"""Сериализация (запись данных в JSON) - это перевод Python Dict в JSON формат (либо сохранить все в файл, либо сохраняем просто как тестовые данные)"""
# dump - метод, записывающий объект Python в файл в формате JSON
# dumps - метод, записывающий объект Python в строку в формате JSON

"""Десериализация (чтение данных из JSON) - это процесс перевода из JSONа в Python dict"""
# load - метод, который считывает файл в формате JSON и переводит его в объекты Python
# loads - метод, который считывает JSON в текстовом формате и переводит его в объекты Python

# ---------------------------------------------------------------------------------------------------------------

# import json
# from urllib.request import urlopen

# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# # print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))

# import json

# with open('downApi.json','r') as file:
#     data = file.read()
#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))

"""Процесс сериализации"""

# import json
# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': None,
#     'children': False,
# }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# import json
# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': None,
#     'children': False,
# }

# string = json.dumps(dict_)
# print(string)
# print(type(string))

# ----------------------------------------------------------------------------------------------

