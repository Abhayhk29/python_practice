from random import random


class Enemy:

    type_of_enemy : str
    health_points : int = 10
    attack_points : int = 1

    def __init__(self):
        pass # This is a placeholder for the constructor, it does nothing but allows us to create an instance of the class without any arguments

    def talk(self):
        print(f'I am an enemy and I have {self.health_points} health points and {self.attack_points} attack points and  type is {self.type_of_enemy}')

    def walk_forward(self):
        print(f'Enemy is walking forward {self.type_of_enemy}')

    def attack(self):
        print(f'Enemy is attacking with {self.attack_points} attack points {self.type_of_enemy}')



class Enemy2:

    def __init__(self, type_of_enemy, health_points = 10, attack_points = 1):
        self.__type_of_enemy = type_of_enemy
        #for private variables we can use __ before the variable name, but it is not truly private, 
        # it is just a convention to indicate that it should not be accessed directly
        self.health_points = health_points
        self.attack_points = attack_points

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy

    def talk(self):
        did__special_attack = random.random() < 0.5
        if did__special_attack:
            self.health_points += 5
            print(f'{self.__type_of_enemy} performs a special attack!')
        else:
            print(f'I am an enemy and I have {self.health_points} health points and {self.attack_points} attack points and  type is {self.__type_of_enemy}')





# different type of constructors
#     def __init__(self, type_of_enemy):
#         self.type_of_enemy = type_of_enemy
# Default constructor
#     def __init__(self):
#         self.type_of_enemy = 'Orc'

#No arguments constructor
#    def __init__(self):




#Encapsulation is the concept of bundling data and methods that operate on that data within a single
#  unit, such as a class. It restricts direct access to some of an object's components,
#  which can prevent the accidental modification of data. 
# In Python, we can achieve encapsulation by using private variables and methods.