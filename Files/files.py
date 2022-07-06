"""Работа с файлами"""

# Каретка - указатель
# Hello world, информация в двоичном коде

# open(<Путь до вашего файла>)

# file = open('/home/janylai/Desktop/ev.22/Files/files.py') #Абсолютный путь
# file = open('files.py')# Относительный путь

# print(file)

# Режимы для работы с файлами
# 1. r /r+ (read)
# 2. w /w+ (write)
# 3. a /a+ (append)
# t, b, x

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))

# file = open('/home/janylai/Desktop/ev.22/Files/text.txt')
# data = file.readlines(16) #16 байтов вернет
# print(data)
# file.close()

# file = open('text.txt', 'w+') #когда мы открываем в таком режиме, он удаляет содержимое и готов внести новые записи
# file.write('Hello world\nMy name is John Snow!,\nKing!')
# print(file.read())
# file.close()

# file = open('text.txt', 'a') #ниче не стирает, просто добавляет. make sure картека в конце
# file.write('\nJohn Snow bastard and King')
# file.close()

# file = open('text1.txt','w')  - несуществующие названия вновь создает
# file.close()

# file = open('text2.txt','a') - несуществующие вновь создает
# file.close()

# file = open('text2.txt','x')
# file.close()


"""Контекстный менеджер - мы облегчаем свою жизнь, например не нужно все время закрывать наш файл"""

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)

# print(file) #owibka

# write 
# writelines 
# ls = ['Hello world!', 'My name is John!', 'I\'m 35 years old!']
# with open('text.txt','w') as f:
#     f.writelines(line + '\n' for line in ls) #принимает итерируемый объект

# file.tell() -> возвращает индекс, где находится каретка (указатель)
# file.seek(<int>) -> Перемещает каретку (указатель) на указанный int(index)

# ---------------------------------------------------------------------------------------------------

# from PIL import Image
# import pytesseract
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
#         print(list_of_imei)
    
#     with open('imeicodes.txt','w') as file:
#         for x in list_of_imei: 
#             for i in x:
#                 file.write(f'{i}\n')

# list_images = ['imei.jpg']
# get_imei_codes(list_images)

