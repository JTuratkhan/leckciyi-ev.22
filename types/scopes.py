"""# Области видимости и пространство имен"""

# Buil-in (встроенная область видимости) - print, len, max, int
# Global (глобальная)
# Enclosed (нелокальная, охватывающая, nonlocal) когда внутри функции есть еще функция
# Local (локальная область видимости)

# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element = 'q'
# # print(element)       
# print_list([1,2,3,4,5])
# print(element

# a = 10 #global
# print #built-in
# def hello(): #global
#     a = 'Hello world' #local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# x = 'global'
# print(x, '1')

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

# def func():
#     print(a)

# a= 'str'
# func()

#LEGB local - enclosed - global - built in

# def func():
#     print(a)
#     a = 5

# a = 'str'
# func()

# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()

# func()

# var = 100 #global variable
# def increment():
#     # var = var + 1 #Try to update a global variable (using increment -> var += 1)
#     # print(var)

# increment()

"""Global -> позволяет изменять значение глобавльной переменной находясь в локальной области видимости."""
"""nonlocal -> позволяет менять значение нелокальной переменной находясь в локальной области видимости."""

# var = 100

# def increment():
#     global var
#     var += 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)

# def counter():
#     num = 0
#     def incrementor():
#         nonlocal num
#         num += 1
#         return num
#     return incrementor

# c = counter()
# print(c)
# print(c()) #1
# print(c()) #2
# print(c()) #3
# c = counter()
# print(c())


# print(len(dir(__builtins__)))
# print(abs(-15)) #Стандартный вызов встроенной фнукции
# abs = 15 #Переопределяю встроенное имя abs в глобальной области
# del abs
# print(abs(-15))

# print(dir(list))
# print(dir(dict))