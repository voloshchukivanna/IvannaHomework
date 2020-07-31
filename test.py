#Task 1
# l = [ "spam", "tampa", "world", "piu"]
# i = 0
# for el in l:
#     if len(el) % 2 == 1:
#         i += 1
#         print(i)


#Task2
# d = {"name": "Lala", "age": 20, "pos": "qa"}
# keys = d.keys()
# for key in d.keys():
#     print (key, ': ', d[key], sep = "")

#Task3
# s = input("Enter: ")
# try:
#     s = int(s)
# except:
#     print('error')

#Task4
# s = input()
# d = {"a":1}
# try:
#     for i in d:
#         print(i, ":", di, sep = "")
#         print("ivanna")
#         print(int(s))
# except TypeError:
#     print("voloshchuk")
#
# finally:
#     print("Finish bla bla")
#
# for i in range(10):
#     print("hello")

#Task5
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(unknown_var)
# finally:
#     print("This")



# while True:
#     a = input("Enter float number: ")
#     if a.isdigit():
#         break
#         print(a)


#Task6
# while True:
#     a = input("Enter number: ")
#     try:
#         a = float(a)
#         break
#     except ValueError:
#         print("error")
# print("yeah")
#
# raise TypeError("not a number")
# print("Ivanka")



#Task7
# def repeat (a, b):
#     c = (a**2 + b**2)**0.5
#     return c
#
# d = repeat(4, 4)
# print(d)


# def repeat (s, count, exclaim = True):
#    result = s * count
#    if exclaim:
#       result = result + '!!!'
#     return result
#
# r = repeat ('Ivanka', 3)
# print(r)




#Homework
# Task 4
#1
# def num():
#     while True:
#         a = input("Enter number: ")
#         try:
#             a = float(a)
#             return a
#         except ValueError:
#             pass
#         else:
#             break
#
# num()


#2
'''строка без пробелов в середине, а вначале и в конце пробелы могут быть'''

# def text():
#     while True:
#         word = input("Enter word: ")
#         word = word.strip()
#         if ' ' not in word:
#             return
#
# text()

#3
'''is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.'''

# def is_year_leap():
#     x = int(input(""))
#     if x % 4 == 0 and x % 100 !=0 or x % 400 == 0:
#         return True
#     else:
#         return False
#
#
# print(is_year_leap())

#4
# def trigon():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     if a >= b + c or b >= a + c or c >= a + b:
#         return False
#     else:
#         return True
#
# print(trigon())

#5
# def trigon():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     if a == b == c :
#         print("Equilateral triangle")
#     elif a == b or a == c or c == b:
#         print("Isosceles triangle")
#     else:
#         print("Not a triangle")
#
# trigon()

# a = input("Enter: ")
# assert len(a) < 10 and len(a) > 10
# print(a)

# def f(a, b, *ll):
#     print(a+b)
#     print(sum(ll))
# f(1, 3, 1, 1, 1, 1)




#Task 1
'''Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов 
(неопределенное количество). Учитываем, что может быть повторяющиеся значения аргументов.'''

# def iv(*numbers):
#     a = list(numbers)
#     a.sort()
#     return a[1]
#
# print(iv(45, 2, 65, 394, 1, 2, 45, 67))



#Task 2

# import re
#
# a = input("Enter: ")
#
# def iv(a):
#     string = re.sub('[^A-Za-z]+', '', a)
#     assert string.isalpha(), "String has symbols!"   # не работает эта строка
#     return string
#
#  print(iv(a))

# from Homework4 import ivanka_song
#
# f = open('lalala.txt')
# x = f.read()
# f2 = open("lalala2.txt", 'w')
# f2.write(ivanka_song(10, 7, 1))
# print(x)


# import requests
# import _json
#
#
# d = {"User_agent": "my-app/0.1"}
# resp = requests.post('http://httpbin.org/post', headers=d, data="ivanna")
# print(resp.text)

# for key in a.headers:
#     print(key)

# import requests
#
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print('Status code: ', r.status_code)
# response_dict = r.json()
# #print(response_dict.keys())
# print("Total repositories:", response_dict['total_count'])
#
# repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))



# import requests
# import _json
#
# url='http://pulse-rest-testing.herokuapp.com/'
# r = requests.get(url)
# print(r.status_code)
#
# book_dict = {
#       'title': "test book 2",
#       'author': "Ivanna Voloshchuk"
#   }
# resp = requests.post(url+'books/', data=book_dict)
# print(resp.status_code)
# req_dict = resp.json()
# for book in req_dict:
#     print(req_dict['id'], req_dict['title'])
# book_id=req_dict['id']
#
# print(req_dict)
#
# r = requests.get(url)
# print(r.status_code)
# book_dict = {
#
#     'title': 'test book 2 change',
#     'author': 'Ivanna Voloshchuk'
#     }
# resp = requests.put(url+'books/'+ str(book_id), data=book_dict)
# print(resp.status_code)
# req_dict = resp.json()
# for book in req_dict:
#     print(req_dict['id'], req_dict['title'])
#
# print(req_dict)

# class Person:
#
#     def __init__(self, name = None, surname = None, age = 0):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def full_name(self):
#         return str(self.name) + " " + str(self.surname)
#
#     def get_older(self, years):
#         self.age += years
#
#     def __add__(self, other):
#         return Person()
#
#
# o = Person("Alex", "Ishchenko", 30)
# o1 = Person()
# print(o.age)
#
# o.get_older(5)
# print(o.age)
#
# print(o + o1)

# o1 = Person()
# print(o.name)
# print(o1.age)
# s = o.full_name()
# print(s)


#o.name = "Ivanna"


# o.method("Ivanna")
# o1.method("Nelly")

# print(o.name)
# print(o1.name)


# o.method(12)
#
#
# o.common.append(500)
# print(o.common)
# print(o1.common)


