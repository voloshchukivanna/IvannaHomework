# Task 1

a = input("Enter: ")

print(a[2], a[-2], a[0:5], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")

# Task 2


# Task 3

x = int(input(""))
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('yes')
else:
    print('no')

# Task 4

a = int(input())
b = int(input())
c = int(input())
if a >= b + c or b >= a + c or c >= a + b:
    print('no')
else:
    print('yes')

# Task 5

a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)

# Task 6

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# Task 7

# 1
a = 0
while a <= 10:
    print(a)
    a += 1

# 2
a = 20
while a >= 1:
    print(a, end=" ")
    a -= 1

# 3

a = [23, 65, 3, 907, 9, 101, 44, 8436, 453, 200, 4]
b = []
c = []

for d in a:
    if d % 2 == 0:
        b.append(d)
    elif d % 2 == 1:
        c.append(d)
else:
    print(d)

print(b)
print(c)


# Task 8

# 1
a = [1, 35, 5, 61, 19, 23, 101]

while a:
    print(a.pop())

print(a)

# 3
a = [1, 35, 5, 61, 19, 23, 101]

while a:
    print(a.sort(reverse=True))
    print(a.pop())

print(a)


# Task 9

a = input()

while True:
    a = input('Enter: ')
    if " " in a:
        break
        print(a)
