# """
# Tuple - это структура данных
# неизменяемый
# индексируемый
# упорядоченный
# """
# функция - это готовая сумка инструментов

# string1 = str('hello AttackPython')
# string2 = 'hello world'
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {1,2}
# dict1 = {"key": "value"}
# tuple11 = (1,2,3)
# print(type(tuple11)) -> tuple class

# много типов данных, потому что они по-разному реагируют

# list1 = [1,2]
# list1[0] = 3
# print(list1)
# tuple1 = 1,2
# tuple1[0] = 3
# # print(type(tuple1))
# print(tuple1[0])

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# # tuple takes less memory
# tuple4 = tuple(range(5))
# print(*range(5))
# * - убирает скобки


# emails = ('Python@gmail.com', 'Tima@mail.ru',3,5,['potato','arbuz','apple'])
# print(type(emails[-1]))
# last_object = emails[-1] # list
# last_object.append(str('Tomato'))
# print(len(emails))


# print(dir(tuple))
# print(*)
# print(dir(list))


# tuple_sequence_first = (2,2,3,4)
# tuple_sequence = tuple(range(5))
# tuple_sequence += tuple_sequence_first
# # # print(tuple_sequence.count(2))
# # print(tuple_sequence.index(3))
# # indx = tuple_sequence.index(3)
# # print(tuple_sequence[indx])


# for value in tuple_sequence:
#     print(value)


# names = ("Tima","Zhanylai", "Aidana", "Bermet", "Ermek")
# print(names[0]+" hello!")
# for name in names:
#     print(f'hello {name.capitalize()}!!!')
#     # print('it is len:', len(name))
# names_enter = ['Bermet','Ermek']
# for name in names_enter:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
#     else:
#         print(f'{name} go home!!!')


# first_step_names = []
# names = input('Введите имя: ').split(' ')
# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)    
# print(first_step_names)


# for i in range(10):
#     print(i)
# print('stop for')
# i = 0

# while 3 > 2:
#     print(f'{i} i work')
#     i +=1

# i=0
# num = 3
# while num>i:
#     print('i work')
#     i+=1





