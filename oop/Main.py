from Enemy import *
from Zombie import *
# from __pycache__.oop.Zombie import Zombie

enemy1 = Enemy()
enemy2 = Enemy()

enemy2.health_points = 40
enemy1.type_of_enemy = 'Orc'
enemy2.type_of_enemy = 'Troll'

enemy1.talk()
enemy2.talk()
enemy1.walk_forward()
enemy1.attack()

print(enemy1.health_points)
print(enemy2.health_points)

print(f'Enemy 1 has {enemy1.health_points} health points and {enemy1.attack_points} attack points {enemy1.type_of_enemy}')


enemy3 = Enemy2('Goblin', 20, 5)
enemy3.talk()
print(enemy3.get_type_of_enemy())
enemy3.set_type_of_enemy('Dragon')
# print(enemy3./())


zombie1 = Zombie('Grognak', 100, 15, 'hi',10)
zombie1.talk()
zombie1.attack()
zombie1.take_damage(20)
