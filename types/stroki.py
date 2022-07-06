# string = строки

# строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации.

# 'Меня зовут Санжар. Мне 20 лет!' - str()

# name = 'John'
# name1 = "John"
# name2 = """
# John
# Snow
# """
# name3 = str("John Snow")
# """Сейчас мы все это выведем в терминал"""

# print(name)
# print(name1)
# print(name2)
# print(name3)

# print(type(name))
# print(type(name1))
# print(type(name2))
# print(type(name3))
# print(type(5))



# Экранирование - механизм при помощи которого можно вставлять символы, которые сложно ввести с клавиатуры.

# \n -> перенос строки
# \t - горизонтальная табуляция
# \f - перевод страницы
# \r - возврат указателя(коретки)
# \v - вертикальная табуляция

# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'
# print(name)
# print(lastName)
# print(last_name)

# name = 'Rachel'
# print(name*3)
# print(name + 'John')



# Индексация символов в строке
# name = 'John'
#         # j = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1

# print(name[0]) #j
# print(name[-1]) #n
# print(name[2]) #h



# Срезы по индексам
# string[start:end:step]
# len() - выводит длину строки
# print(len('Hello world!'))
# name = 'John Snow'
# print(len(name))

# text = 'Hello world! My name is John Snow!'
# print(text[0:5])
# print(text[13:-1])
# print(text[13:])
# print(text[::2])
# print(text[::-1])
# print(text[::-2])
# print(text[:14:-1])



# конкатенация строк (слияние, соединение)

# word1 = 'Hello'
# word2 = 'world'
# probel = ' '

# result = word1 + probel + word2
# print(result)
# print(word1 + probel + word2 + '!!!')
# # print(word1, probel, word2, '!!!')
# str1 = word1, word2, probel
# print(str1)
# print(type(str1))



# Форматирование строк
# 1. с помощью знака %
# 2. с помощью .format()
# 3. Интерполяция строк(f-строки)

# %
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello, mr/mrs %s %s' %(name, last_name))

# .formst
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello, mr/mrs {} {}'.format(name, last_name))

# # f-строки
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print(f'Hello, mr/mrs {name} {last_name}')
# print('Hello, mr/mrs', name, last_name)
# print('Hello, mr/mrs' + name + " " + last_name)

# r = 'daniel'
# r1 = str.swapcase(r)
# print(r1)

# text = 'abracadabra'
# text = text[0:5] + 'K' + text[6:]
# print(text)