# map()
# filter()
# lambda()
# enumerate()


# Анонимные функции - lambda(такие же функции только без названия)
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражение

# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args1(a,b): return a + b

# print(sum_args(1,2))
# print(sum_args1(1,2))

# sum_arg = lambda a,b: a + b
# print(sum_arg(1,2))

# x = lambda a,b,c: a + b + c
# print(x(5,6,7))

# import random

# ls = ['plov','manty','kuurdak','lagman','dymdama']
# p=0
# m=0
# k=0
# l=0
# d=0
# for i in range(0,100000):
#     choice= random.choice(ls)
#     # print(choice)
#     if choice.lower() == 'plov':
#         p= p+1 #p+=1 инкремент 
#     elif choice.lower() == 'manty':
#         m+=1 
#     elif choice.lower() == 'kuurdak':
#         k+=1
#     elif choice.lower() == 'lagman':
#         l+=1
#     elif choice.lower() == 'dymdama':
#         d+=1

# # print(f'Plov:{p},\nManty:{m},\nKuurdak:{k},\nLagman:{l}')
# dict_ = {'Plov': p, 'Manty': m, 'Kuurdak': k,'Lagman': l, 'Dymdama': d}
# # print(dict_.items())
# result = sorted(dict_.items(), key=lambda x: x [1])
# # print(result)
# winner = result[-1]
# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]}')


# ls = ['def','ivan', 'john', '',' ']
# ls2 = sorted(ls,key=len)
# print(ls2)

# map(function, Iterable) -> применяет функцию к каждому элементу последовательности и возвращает mapobject(итератор) с результатами.

# например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
# list_of_words = ['one','two','three','dict']
# result = list(map(str.upper,list_of_words))
# print(result)
# result2 = list(map(len, list_of_words))
# print(result2)


# ls = ['1','2','3','4']
# result = list(map(int,ls))
# print(result)

# names = ['John','Jamie','Sansa','Thyrion','Aibek']
# # ['Hello mr/mrs John', 'Hello mr/mrs Jamie'...]
# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)

# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]
# #100,400,900,1600,2500

# result = list(map(lambda x,y: x*y, nums, nums2))
# print(result)

# dict_ = {1:2, 3:4, 5:6}
#         #{1:'2',3:'4',5:'6'}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)


# ---------------------------------------------------------------------------

# filter(function, Iterable) - применяет ко всем элементам iterable функцию, которую мы передаем и возвращает filterobject(итератор) с теми объектами, для которых функция вернула True.

# from unittest import result


# list_of_str = ['one','two','list','','100','1','50','John99']
# result = filter(str.isdigit, list_of_str)
# print(list(result))
# for x in result:
#     print(x)


# ls = [10,11,102,213,314,515]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)

# list_of_words = ['John','one','two','list','makers','ev.22','ono']
# result = list(filter(lambda x: len(x) >= 4, list_of_words))
# print(result)

# ------------------------------------------------------------------

# enumerate(iterable)

# ls = ['str1','str2','str3']
# i = 0
# # for x in ls:
# #     print(f'element: {x}, index {i}')
# #     i+=1

# for i, x in enumerate(ls):
#     print(f'element: {x}, index: {i}')

# new_list = list(enumerate(ls))
# print(new_list)

# Hackerrunk
# def counting_valleys(n, s):
#     current_level = 0
#     count = 0
#     for i in range(n):
#         if s[i] == 'U':
#             current_level += 1
#         elif s[i] == 'D':
#             current_level -= 1
#             if current_level == -1:
#                 count += 1
#     return count

# n = int(input().strip())
# s = input().strip()
# result = counting_valleys(n, s)
# print(result)