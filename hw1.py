# Задача 2: Найдите сумму цифр трехзначного числа. 

# n = int(input("Vvedite trexznachnoe chislo: "))
# while n < 100 or n > 999:
#     n = int(input("Vvedite trexznachnoe chislo: "))
# n1 = n // 100
# n2 = (n % 100) // 10
# n3 = n % 10
# print(n1 + n2 + n3)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# n = int(input("Vvedite kol-vo zyravlikov: "))
# x = n // 6
# print(x, 4 * x, x)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# n = int(input("Vvedite nomer bileta: "))
# n1 = n // 100000
# n2 = (n // 10000) % 10
# n3 = (n // 1000) % 10
# n4 = (n % 1000) // 100
# n5 = (n % 100) // 10
# n6 = n % 10
# if n1 + n2 + n3 == n4 + n5 + n6:
#     print('YES!')
# else:
#     print('No(')

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Vvedite shiriny chocolatki: "))
m = int(input("Vvedite dliny chocolatki: "))
k = int(input("Kol-vo dolek: "))
if k <= n * m and (k % m == 0 or k % n == 0):
    print('Yes')
else:
    print('no')
