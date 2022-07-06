# методы строк

# dir() - функция, которая вытаскивает методы типов данных
# print(dir(str))


# '<соединитель>' .join(<массив который нужно соединить>) - Соединяет массив из строк по соединителю в одну строку.
# ls = ['milk', 'bread','water','apple','5']
# joined = '###'.join(ls)
# print(joined)



# split(разделитель) -> Дробит строку по разделителю и возвращает тип данных list.
# text = 'Milk, Bread, Water, Apple'
# splited = text.split(',')
# print(splited)
# joined = ', '.join(splited)
# print(joined)



# replace(<old value>,<new value>, [count])-> Меняет в строке значение old на new value, если вы укажете count, то он заменит count раз.
# text = 'ha ha ha ha ha'
# result = text.replace('ha','la')
# print(result)
# print(text)

# result = text[:3] + text[3:].replace('ha','la')
# print(result)
# print(text)



# strip() - Убирает пробельные символы в начале и в конце строки.

# rstrip() - в конце удаляет (справа)
# lstrip() - в начале удаляет (слева)

# text = input('Введите ФИО')
# result = text.lstrip()
# print(text.strip())
# print(result)
# # print(text)



# count('<symbol>') -> считает количество вхождений <symbol> в строку

# text = 'Hello world! I\'m from Earth!'
# result = text.count('l')
# print(result)



# index('<value>', [start], [end]) -> выводит индекс значения value в нашей строке.
# text = 'Hello World! This is Makers!'
# result = text.index('is')
# print(result)
# print(len(text))
# print(text.find('T'))



