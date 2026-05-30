from Enemy import *

class Zombie(Enemy2):
    
    def __init__(self, type_of_enemy, health_points, attack_points, name, health):
        super().__init__(type_of_enemy=type_of_enemy, 
                         health_points=health_points, 
                         attack_points=attack_points)
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with a bite!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")