# 2. Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def int_to_hex(number):
    return hex(number)

input_number = int(input("введите целое число: "))
hex_string = hex(input_number)
print("шестнадцатеричное представление числа с помощью функции hex:", hex_string)

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def calculate_fraction(fraction1, fraction2):
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)

    sum_fraction = fraction1 + fraction2
    product_fraction = fraction1 * fraction2

    return sum_fraction, product_fraction

input_fraction1 = input("Введите первую дробь (вида а/b): ")
input_fraction2 = input("Введите вторую дробь (вида а/b): ")

sum_fraction, product_fraction = calculate_fraction(input_fraction1, input_fraction2)
print("Сумма двух дробей:", sum_fraction)
print("Произведение двух дробей:", product_fraction)


from fractions import Fraction

fraction1 = Fraction("1/2")
fraction2 = Fraction("3/4")

sum_fraction = fraction1 + fraction2
product_fraction = fraction1 * fraction2

print("Сумма дробей с помощью модуля fractions:", sum_fraction)
print("Произведение дробей с помощью модуля fractions:", product_fraction)
