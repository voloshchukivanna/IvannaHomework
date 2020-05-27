# TASK 1
# 1
a = "IvannaVoloshchuk"
a.isdigit()

# 2
a = "Ivanna Voloshchuk qa    "
a.count(" ")

# 3
s = "....test..qa....auto...2"
s.count(".")

# 4
k = "Homework"
k.center(100)

# 5
s = "ivanna voloshchuk done homework task 1"
s.title()
s1 = s.title()

# 6
g = "he was reading 'never eat along'"
g.endswith("ing")

# 7
d = "Ivanna"
d.find("a")

# 8
a = "a b c d f"
a.split()

#TASK 2

#1
a = 367
b = 127
c = (a**2 + b**2)**0.5
print(c)

#2
# a = 57
print(a//10%10)

#3
print(sum([4,5,6]))   #не разобралась с этой функцией sum. Как мне написать такой цикл с помощью функции sum: a = 456 print(sum(a, [4, 5, 6]))?

#4
n = 3
print(n + 2 - (n%2))

#5
x = 3.5
print(s%1)

#6
a = float(34.345)
print(int(a*10)%10)

#TASK 3

#1
cars = ['bmw', 'audi', 'honda', 'nissan']
print(cars[-3])

#2
cars = ['bmw', 'audi', 'honda', 'nissan']
a = cars[1]
print(a[:1])

#3
cars = ['bmw', 'audi', 'honda', 'nissan']
b = cars[-1]
print(b[-1:])

#4
cars = ['bmw', 'audi', 'honda', 'nissan']
cars.append('infiniti')
print(cars)

#5
cars = ['bmw', 'audi', 'honda', 'nissan']
print(len(cars))
cars.insert(2, 'infiniti')
print(cars)

#6
cars = ['bmw', 'audi', 'honda', 'nissan']
del cars[0]
print(cars)

#7
cars = ['bmw', 'audi', 'honda', 'nissan']
cars.remove('honda')
print(cars)

#TASK 4

#1
d = {"title": "female", "price": 3200, "ingredients": "suit"}
d["description"] = "coton"
print(d)

#2
d = {"title": "female", "price": 3200, "ingredients": "suit"}
d["price"] += 100
print(d)

#3
d = {"title": "female", "price": 3100, "ingredients": "suit"}
d["ingredients"] += ", shirt"
print(d)

#4
d = {'title': 'female', 'price': 3100, 'ingredients': 'suit, shirt]'}
len(d["ingredients"].split())

#5
d = {'title': 'female', 'price': 200, 'ingredients': 'suit', 'description': 'coton'}
del d['description']
print(d)

