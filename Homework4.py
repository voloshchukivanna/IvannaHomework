#Task 1

a = input("Enter: ")

try:
   print(a[2], a[-2], a[0:5], a[:-2], a[::2], a[1::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep="\n")
   print("Верно!")
except SyntaxError:
   print("Строка слишком коротка!")


#Task 2

a = input("Enter number 1: ")
b = input("Enter number 2: ")

try:
   print(float(a)+float(b))
except ValueError:
   print(str(a)+str(b))


#Task 3

def ivanka_song(a = 3, b = 3, c = 0):
   for i in range(0, a):
       if c == 1:
           print("-".join(["la"]*3) + "!")
       else:
           print("-".join(["la"]*3) + ".")

ivanka_song()

#Task 4

#1
def num():
    while True:
        a = input("Enter number: ")
        try:
            a = float(a)
            return a
        except ValueError:
            pass
        else:
            break

num()

#2
def text():
    while True:
        word = input("Enter word: ")
        word = word.strip()
        if ' ' not in word:
            return

text()

#3
def is_year_leap():
    x = int(input(""))
    if x % 4 == 0 and x % 100 !=0 or x % 400 == 0:
        return True
    else:
        return False


print(is_year_leap())

#4
def trigon():
    a = int(input())
    b = int(input())
    c = int(input())
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

print(trigon())

#5
def trigon():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b == c :
        print("Equilateral triangle")
    elif a == b or a == c or c == b:
        print("Isosceles triangle")
    else:
        print("Not a triangle")

trigon()