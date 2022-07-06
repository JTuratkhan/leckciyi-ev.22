"""1"""
# a = {'x':1,'y':2,'z':1}
# print(a.get('z'))

# a = {'a':1,'b':2,'c':1}
# deleted = a.pop('a')
# print(deleted)

# a = {'a':1,'b':2,'c':1}
# a['f'] = 55
# print(a)

# a = {'a':1,'b':2,'c':1}
# a.clear()
# print(a)

# a = {'a':1,'b':2,'c':1}
# for i in a.keys():
#     print(i)

# a = {'a':1,'b':2,'c':1}
# v = []
# for i in a.keys():
#     v.append(i)
# print(v)

# a = {'a':1,'b':2,'c':1}
# b = a.copy()
# print(b)

# a = {'a':1,'b':2,'c':1}
# for i in a.keys():
#     print(i)

# a = {'a':1,'b':2,'c':1}
# for i,j in a.items():
#     print(i,j)



# a = {'x': 1, 'y': 2, 'z': 1}

# for x in a.keys():
#     print(x)
#     break


# a = {'x': 1, 'y': 2, 'z': 1}

# for i in a.keys():
#     pass
# print(i)

# print(dir(int))

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# a1 ={}
# for k,v in a.items():
#     a1[k] = v / 5
# print(a1)

# a = {'a': 1, 'b': 2, 'c': 3} 
# new_a = {}
# for k,v in a.items():
#     new_a[v] = k
# print(new_a)


# a = {'a': 3, 'b': 2}
# for v in list(a.values()):
#     list_ = sum(list(a.values()))
# print(list_)

# d = dict([(1,1),(2,4)])
# print(d)

# list_ = [[1,2,3],[3,3,5],[5,6,5],[12,3,34]]
# # sums = []
# # for x in list_:
# #     sums.append(sum(x))
# # print(sums)
# # print(max(sums))
# res = max([sum(x) for x in list_])
# print(res)

# -----------------------------------------------
# alice = [13, 15, 38]
# john = [5, 15, 50]
# res = {'Alice':1, 'John': 1}

# [33,55,10]
# [33,66,10] # 0 0
# [54,20,10]
# [10,35,15] #1,2


# alice = [54, 20, 10]
# john = [10, 35, 15]

# def compareScores(a,j):
#     score_a = 0
#     score_j = 0
#     for i in range(0, len(a)):
#         if a[i] > j[i]:
#             score_a += 1
#         elif j[i] > a[i]:
#             score_j += 1
#         else:
#             pass
#     return {'Alice':score_a, 'John': score_j}

# print(compareScores(alice,john))
# print(compareScores([54,20,10], [10,35,15]))


# str_ = 'pythoniiist'
# # dcit_ = {'p': 1, 'y':1, 't':2, 'i':3}
# dcit_ = {key:str_.count(key) for key in str_}
# print(dcit_)

# dict_ = {key : key**2 for key in range(1,11) }
# print(dict_)

# n = int(input('Введите число от 1 до 10'))
# dict_ = {key : key**2 for key in range(1,501) if key % n == 0}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key : [value for value in range(1, value+1)] for key,value in a.items()}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# dict_new = {key : 'odd' if value % 2 != 0 else 'even' for key, value in dict_.items()}
# print(dict_new)

# string_ = ('In 1984 there were 13 instances of a protest with over 1000 people attending')
# a = string_.split()
# print(a)
# list_ = [z for z in a if z.isdigit()]
# print(list_)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},'Olga': {'history': 92, 'math': 96, 'literature': 81},'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# # new_dict1 = {key : {inner_key : inner_value for inner_key, inner_value in value.items()} for key, value in dict_.items()}

# new_dict = {key1: key2 for key1, val1 in dict_.items() for key2, val2 in val1.items() if val2 == max(val1.values())}
# print(new_dict)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {key : value2 for key, value in my_dict.items() for key2, value2 in value.items()}
# print(dict_)