"""
///////////// 47:23 Основные типы

str 'Amir'
int 10
bool True
list [1, 2, 3]
dict {'min': 5, 'max': 12}


///////////// 56:40 Встроенные функции

print()     type()      id()
len()       sum()       input()
round()     min()       bool()
int()


///////////// 1:03 Функция dir и атрибуты объектов

name = 'Amir'
print(dir(name))
print(name.upper())


///////////// 1:08 Встроенные функции print & dir

print(dir(__builtins))


///////////// 1:16 Встроенная функция input и методы строк
name = input('Enter your name: ')
print(12)
print(name.capitalize())



"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Ошибка: деление на ноль")
    return None


print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = None

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    print("Ошибка: некорректный выбор операции")

    print('Second commit')
