# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#from random import randint
#def get_list(a, first, last):
#    return [randint(first, last) for i in range(a)]
#def odd_sum(list):
#    return sum(list[1::2])
#a = 5
#first = 1
#last = 5
#
#list = get_list(a, first, last)
#print(list)
#print(odd_sum(list))

#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

#from random import randint
#
#num = int(input('Enter list size: '))
#list = []
#list_2 = []
#for i in range(num):
#    list.append(randint(0, 100))
#for i in range(len(list)):
#    while i < len(list)/2 and num > len(list)/2:
#        num = num - 1
#        a = list[i] * list[num]
#        list_2.append(a)
#        i += 1
#
#print(list)
#print(list_2)

#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#from random import uniform
#
#def get_real_nums (a, first, last):
#    return [round(uniform(first,last), 2) for i in range(a)]
#def find_diff(num1):
#    n = [round(x - int(x), 2) for x in (num1)]
#    return max(n) - min(n)
#a = 5
#first = 1
#last = 10
#num1 = get_real_nums(a, first, last)
#
#print (num1)
#print(find_diff(num1))

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

#a = int(input('Enter the number: '))
#n = ''
#while a > 0:
#    n = str(a%2) + n
#    a = a // 2
#print(n)

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#k = int(input('Enter the number: '))
#
#if k < 0: k = k * -1
#num1 = num2 = 1
#list = [num1, num2]
#
#for i in range(2, k):
#    num1, num2 = num2, num1 + num2
#    list.append(num2)
#num1 = num2 = 1
#
#for i in range(-k, 1):
#    num1, num2 = num2, num1 - num2
#    list.insert(0, num2)
#
#print(list)