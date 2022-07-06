# Операторы сравнения
# Условные операторы
# Логические операторы


# Операторы сравнения:
# <,>,== (равно),<=,>=,!=(неравно)

# num1 = 15
# num2 = 15
# stroka1 = 'h'
# print(ord(stroka1)) аски код
# stroka2 = 'a'
# print(ord(stroka2)) аски код
# result = stroka1 > stroka2
# print(result)
# bool -- True(1) or False(0)
# print(chr(1080)) показывает аски код



# Условные операторы
# if
# elif
# else

# if <condition>: если сегодня солнце, то я устрою пикник
#     если в if приходит True
#     <body if>
# elif <>: если облачно, то я погуляю
#     <body>
# else: если ни то, ни другое. я останусь дома.
#     <body>


# string = input('Enter sth: ')

# if string == 'Hello':
#     print('Hello stranger')
# elif string == 'Mercedes':
#     print('Mercedes Benz S class')
# else:
#     print('Совпадений не найдено')

# print('Код закончился')


# sign up
# email = input('Enter email:')
# password1 = input('Enter password:')
# password2 = input('Enter password confirmation:')
# if password1 != password2:
#     raise Exception('Passwords didn\'t match!!!')
# else:
#     print('Successfully signed up!')


# age = input('Enter your age: ')
# # print(type(age))
# if age.isdigit():
#     age = int(age)
# else:
#     print('Введите корректные данные')
#     raise Exception('Value error')

# if age < 18:
#     print(f'Chuvak prihodi cherez {18-age} goda/let')
# else:
#     print('Vy podhodite po vozrastu')


# Логические операторы
# 1. and -> логическое "и"
# 2. or -> логическое "или"
# 3. not -> логическое отрицание

# my_age = 20
# your_age = 18
# result = (my_age == 20) and (your_age == 19)
# print(result)

# result = my_age > 18 or your_age == 20
# print(result)

# result = not my_age != 20
# print(result)



# is_user_google_user = True
# is_user_github_user = True
# is_user_age_greater_21 = False
# user_accounts_coins = 2000

# if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins > 5000):
#     print('You can enter the system mr John Snow')
# else:
#     print('Sorry, you couldnt enter')

# a = '#makers#bootcamp#coding#camp#'
# b = a.strip('#')
# print(b.split('#'))