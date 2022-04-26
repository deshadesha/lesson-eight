#Черновик

    #Задание a
list = [i for i in range(0, 500) if len(str(i)) == 2 and 10 < i < 20]
print("0/ Лист", list)

    #Задание b
from functools import reduce
print("1/ Максимум списка чисел", reduce(max, list))
print()

    #Задание c
print("2/ Сумма всех чисел списка", sum(list))
print()

    #Задание d
print("3/ Произведение всех чисел списка", reduce(lambda x, y: x*y, list))
print()

    #Задание e
import math
print("4/ Факториал какого числа вас интересует?")
num = int(input())
print("Факториал вашего числа", math.factorial(num))
print()

    #Задание f
import random
import string

print("5/ Какую длину строки хотите увидеть?")
l = int(input())

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))
print("Вот она ваша строка", randStr(N=l))
print()


    #Задание g


    #Задание h
def PascalTriangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[left+right for left,right in zip(trow+y, y+trow)]
   return n>=1

print("6/ Сколько строк треугольника Паскаля требуется?")
nn = int(input())
PascalTriangle(nn)





