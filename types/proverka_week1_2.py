# seconds_in_minutes = 60
# minutes_in_hours = 60
# seconds_in_hours = seconds_in_minutes*minutes_in_hours
# hours_in_day = 24
# seconds_in_day = hours_in_day*seconds_in_hours
# days_in_year = 365
# seconds_in_year = seconds_in_day*days_in_year
# print(seconds_in_year)

# months_in_year = 12
# seconds_in_months = seconds_in_year/months_in_year
# print(seconds_in_months)

# a = pow(2,2)
# print(a)

# first = 1
# second = 2
# third = 3
# first, third, second = second, first, third
# print(first)
# print(second)
# print(third)

# s = 'spameggs'
# # print(s[::-1])
# print(s[-3:-5:-1])

# string = 'Cinderella'
# new_string = string[0]
# new_string1 = string[-1]
# p = string[1:-1]

# string = 'Hello'
# new_string = string[0]
# new_string1 = string[-1]
# p = string[1:-1]
# print(new_string1 + p + new_string)


# string = input()
# if len(string)>5:
#     print('True')
# else:
#     print('False')


# x = 4
# y = 7
# z = 3
# if x<y and x<z:
#     print(x)
# elif y<x and y<z:
#     print(y)
# else:
#     print(z)

# x = 200
# y = 560
# z = 561
# if x==z and x==y and z==y:
#     print('3')
# elif x==z or z==y:
#     print('2')
# else:
#     print('0')

# x = int(input())
# y = int(input())
# if x%y != 0:
#     print('x не делится на y')
#     print(x//y)
#     print(x%y)
# else:
#     print('x делится на y')
#     print(x//y)


# year = int(input())
# if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# if not chr(num).isalpha():
#     print(f'Это не буква, а символ "{chr(num)}"')
# else:
#     print(f'Это буква "{chr(num)}"')

# count = 0
# number = input()
# if number.isdigit():
#     count += int(number)
#     print(count)
# else:
#     print('Введите число')

# print((1,2,3)<(1,2,4))
# print((12>40) or (400>=400))

# name_of_list = ['Helloworld!']
# new_list = []
# string = name_of_list.pop()

# if len(string) % 2 != 0:
#     new_list.extend(string[len(string)//2 + 1:])
#     new_list.extend(string[:len(string)//2 + 1])
# else:
#     new_list.extend(string[len(string)//2:])
#     new_list.extend(string[:len(string)])

# print(new_list)

# list_ = ['a','b']
# new_list = []
# list_.reverse()
# new_list.extend(list_)
# print(new_list)

# list_ = ['a','b']
# list_.reverse()
# new_list = list_
# print(new_list)

# suitcase = []
# suitcase.append('Lifchik')
# suitcase.append('Trusy')
# suitcase.append('Krem')
# suitcase.append('Shlyapa')
# suitcase.append('Paren')
# print(suitcase)
# suitcase.pop()
# print(suitcase)
# suitcase.insert(0,'Tufli')
# print(suitcase)


# nums = [1,2,3,4,5,6]
# res = []
# for x in nums:
#     if x < 5:
#         res.append(x)
# print(res)

# values = input()
# ints_as_strings = values.split(',')
# ints = map(int, ints_as_strings)
# list_ = list(ints)
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# list_ = ['world','hello']
# list_.reverse()
# new_list = list_
# print(new_list)

# list_ = [1,2,3,4,5]
# new_list = []
# for x in list_:
#     new_list.append(str(x))
# print(new_list)


# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)

# a = input()
# comma = a.split(',')
# int_ = map(int,comma)
# list1 = list(int_)
# list_ = []
# for i in list1:
#     list_.append(str(i))
# print(sorted(list_))

# list_ = [1,1,4]
# if list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
#     print('yes')
# else:
#     print('ERROR')

# list_ = list(range(55,9185,5))
# print(list_)

# for i in range(1,10):
#     i -= 5
# print(i)

# a = list('py')
# print(len(a))

# a = [1,3]
# print(int(a))

# for i in range(9,4,-3):
#     print(i)