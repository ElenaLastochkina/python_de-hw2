# 2. Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

decimal_number = int(input("введите целое число: "))
hex_number = hex(decimal_number)
print("шестнадцатеричное представление числа:", hex_number)

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

fraction1_str = input("Введите первую дробь (вида а/b): ")
fraction2_str = input("Введите вторую дробь (вида а/b): ")

fraction1 = Fraction(fraction1_str)
fraction2 = Fraction(fraction2_str)

sum_fraction = fraction1 + fraction2
product_fraction = fraction1 * fraction2

print("Сумма двух дробей:", sum_fraction)
print("Произведение двух дробей:", product_fraction)