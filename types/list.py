# list()(список, массив) - изменяемый, последовательный тип данных, который из себя представляет коллекцию каких-либо объектов (данных).

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# 1. -> list(<iterable>)
# my_list = list('Hello world')
# print(my_list)
# my_list = list(54) >>> is not iterable, error
# print(my_list)
# tuple_ = ('banana','apple', 'cherry')
# print(tuple_)
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))

# 2. range() -> возвращает последовательность элементов(числа)
# a = range(15)
# print(a)

# a = list(range (5,15))
# print(a)

# a = list(range (1,100,2))
# print(a)

# 3. -> []

# my_list = [1,23,4,45,5]
# print(type(my_list))
# print(my_list)

# print(dir(list))

# append (element) - добавляет элемент в конец списка
# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)


# extend(element[interable]) -> раздробил, расширяет список добавляя element в конец.
# list_ = [1,2,3]
# list_.extend('hello')
# print(list_)

# insert(<index>,<element>) -> добавляет element по указанному index
# list_ = ['string', 2,3, False]
# list_.insert(1, [1,2,3])
# print(list_)

# list_ = ['string', 2,3, False]
# list_.insert(1, [1,2,3, None])
# list_.insert(2,1)
# print(list_)
# print(list_[5])
# print(list_[1][3])
# print(list_[2:5]) - срезы, вытащить от этой сифры до такого то


# index(element,[start],[end]) - возвращает индекс elementа
# ls = [1,2,33,3,4,5,5,7,2,'hello']
# print(ls.index(5, 6))

# if 'hello' in ls:
#     print(f'"hello" is in list: {ls.index("hello")}')
#     print('"hello" is in list:', ls.index("hello"))

# count(element) -> Возвращает количество вхождений element в списке
# ls = [1,2,3,4,5,5,5,5,5,1]
# result = ls.count(1)
# print(result)


# remove(element) - удаляет element, но если такого элекмента нет в списке, то выводит ошибку
# pop([index])- удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент.
# list_ = [5,1,2,3,4,5]
# # list_.remove(5)
# # list_.remove(5)
# # list_.remove(5)
# deleted = list_.pop(1)
# d = list_.remove(4)
# print(list_)
# print(deleted)
# print(d)


# # sort([reverse = True/False], [key=<>]) -> сортирует список. Если в аргументах передан reverse=True то список будет отсортирован  в убывающем порядке.
# ls = [5,0,-2,-101, 102, 23, 1]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls = ['hello','john','London','a']
# # ls.sort()
# # print(ls)

# ls.sort(key=len, reverse=True)
# print(ls)

# ls = [1,'h',3]
# ls[1] = 2
# print(ls)

# ls = [1,'h',3]
# ls[1] = 2
# print(ls)
# del ls[-1]
# print(ls)

