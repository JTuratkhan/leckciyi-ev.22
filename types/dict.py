"""methods"""

# 1.get(key, None)
# my_dict = {1:'Tom',2:'John',3: 'Alice'}
# print(my_dict.get(3))
# # print(my_dict[3]) 
# print(my_dict.get(4)) # этот показывает None
# print(my_dict[4]) # этот показывает Эррор
# print(my_dict.get(4, 'no such key in my dict'))

# 2.clear()
# my_dict = {1:'Tom',2:'John',3: 'Alice'}
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# 3.copy()
# my_dict = {1:'Tom',2:'John',3: 'Alice'}
# my_dict2 = my_dict.copy()
# my_dict[2] = 'Rachel'
# print(my_dict)
# print(my_dict2)

# 4.pop(key, default)
# dict_ = {'name':'Kate','height':170,'weight':50}
# # deleted = dict_.pop('weight')
# deleted = dict_.pop('age', 'no such key in dictionary')
# print(dict_)
# print(deleted)

# 5.popitem()
# dict_ = {'name':'Kate','height':170,'weight':50}
# dict_.popitem()
# print(dict_) начиная с версии 3.8 пайтон удаляет последнее значение словаря, несмотря на то, что он является неупорядоченным

# 6.setdefault(key, default)
# dict_ = dict(a=1,b=2,c=3)
# print(dict_)
# print(dict_.setdefault('d',5))
# print(dict_)
# print(dict_.setdefault('c',5))
# print(dict_)

# 7.update()
# dict1 = {1:'Tom', 2:'Alice'}
# dict2 = {2: 'Bob', 4: 'Ann'} #если у нас есть два одинаковых ключа, прежний перезаписывается на новый
# dict1.update(dict2)
# print(dict1)
# print(dict2)

# 8.fromkeys(sequence, value)
# numbers = [1,2,3,4,5]
# new_dict = dict.fromkeys(numbers,'Makers')
# print(new_dict)

# numbers = list('makers') #функция лист берет символы строки и возвращает каждый как элемент
# new_dict = dict.fromkeys(numbers)
# print(new_dict)


"""Перебор элементов словаря"""
# items(),keys(),values()

# dict_ = {'name':'Kate','height':170,'weight':50}
# print(dict_.items()) #возвращает списки, внутри кортежа с ключом и значением
# print(dict_.keys())
# print(dict_.values())

# contacts = {
#     'Alice':'+996700631284',
#     'John':'+996500090909',
#     'Sam':'+996555989898'
# }
# # for info in contacts:
# #     print(info)
# for key in contacts.values():
#     print(f'Name: {key}')

# nested_dictionary = {
#     'Makers':{
#         'Aibek':23,
#         'Adilet':27,
#         'Aidai':21,
#         'Nurbek':{
#             'age':18,
#             'height':190,
#             'weight':80
#         }
#     }
# }
# print(nested_dictionary['Makers']['Nurbek']['height'])

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for k, v in a.items():
#     if v % 2 == 0:
#         b[k] = 2
#     else:
#         b[k] = v
# print(b)

# a = {'apple': 2, 'orange': 5, 'banana': 10} 

# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)

# print(a)