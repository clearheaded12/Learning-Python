"""
///////////// 47:23 основные типы

str 'amir'
int 10
bool true
list [1, 2, 3]
dict {'min': 5, 'max': 12}


///////////// 56:40 встроенные функции

print()     type()      id()
len()       sum()       input()
round()     min()       bool()
int()

///////////// 1:03 функция dir и атрибуты объектов

name = 'amir'
print(dir(name))
print(name.upper())


///////////// 1:08 встроенные функции print & dir

print(dir(__builtins))


///////////// 1:16 встроенная функция input и методы строк
name = input('enter your name: ')
print(12)
print(name.capitalize())



"""


class Person:
    """ Model of a person """

    def __init__(self, name, age, height):
        """Initialization of person attributes – name, age"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Get person description"""
        description = self.name + ' ' + str(self.age) + ' ' + str(self.height) + ' ' + str(self.weight)
        print('The new man`s name is ' + description)

    def get_weight(self):
        print('The weight of our person is ' + str(self.weight))

    def update_weight(self, kg):
        self.weight = kg


class Warrior(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        print('Frenzy rage is ' + str(self.rage))


warrior = Warrior('Conan', 32, 2.13)
warrior.get_rage()
# warrior.update_weight(150)
# warrior.description_person()

# man = Person('Amir', 21, 187)
# man.description_person()
# woman = Person('Masha', 19, 160)
# woman.update_weight(60)
# woman.get_weight()
