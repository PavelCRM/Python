#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.

num: int = int(input("Введите целое число: "))
def hex_number(num: int, mod: int = 16) -> str:
    res = ''
    while num != 0:
        temp = num % mod if (num % mod) < 10 else chr(num % mod + 87)
        res = str(temp) + res
        num //= mod
    res = "0x" + res
    return res    
print(f'''hex of number = {hex_number(num)}
test with hex() = {hex(num)}''')

#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
from math import gcd

f1 = input('Введите первую дробь: ')
f2 = input('Введите вторую дробь: ')

frac_1 = Fraction(f1)
frac_2 = Fraction(f2)
sum_frac = frac_1 + frac_2
mult_frac = frac_1 * frac_2 
# функция нахождения НОД
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# функция нахождения суммы дробей
def add_fractions(f1, f2):
    numerator1, denominator1 = map(int, f1.split('/'))
    numerator2, denominator2 = map(int, f2.split('/'))
    lcm = denominator1 * denominator2 // gcd(denominator1, denominator2) # НОК
    numerator_sum = numerator1 * (lcm // denominator1) + numerator2 * (lcm // denominator2) 
    return str(numerator_sum) + '/' + str(lcm)
# функция нахождения произведения дробей
def multiply_fractions(f1, f2):
    numerator1, denominator1 = map(int, f1.split('/'))
    numerator2, denominator2 = map(int, f2.split('/'))
    numerator_product = numerator1 * numerator2
    denominator_product = denominator1 * denominator2
    return str(numerator_product) + '/' + str(denominator_product)
print(f'''Сумма дробей: = {add_fractions(f1, f2)}
Проверка суммы дробей: = {sum_frac}''')
print(f'''Произведение дробей: = {multiply_fractions(f1, f2)}
Проверка произведения дробей: = {mult_frac}''')

        