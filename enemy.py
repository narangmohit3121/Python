import time
import random


class Enemy(object):

    def __init__(self, name, hit_points=1, number_of_lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = number_of_lives
        self._default_hit_points = hit_points
        self._isDead = False

    def __get_hit_points__(self):
        return self._hit_points

    def __set_hit_points__(self, points):
        self._hit_points = points
        # self._default_hit_points = points
        # print("Default points are", self._default_hit_points)

    hitPoints = property(__get_hit_points__, __set_hit_points__)

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points > 0:
            self._hit_points = remaining_points
            print('Remaining points of {0._name} are {0._hit_points}'.format(self))
        else:
            remaining_lives = self._lives - 1
            if remaining_lives == 0:
                self._lives = 0
                print('{0._name} is dead'.format(self))
            else:
                self._lives = remaining_lives
                print("Remaining lives of {0._name} are {0._lives}".format(self))
                self._hit_points = self._default_hit_points
                print("Default points are", self._default_hit_points)

    @property
    def lives(self):
        return self._lives

    @property
    def isDead(self):
        return self._isDead


class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=20, number_of_lives=3)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name, hit_points):
        super().__init__(name=name, hit_points=hit_points, number_of_lives=2)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("No Dodge")
            return False
        else:
            print("{0._name} dodged the attack".format(self))
            return True

    def take_damage(self, damage):
        if self.dodges() is not True:
            super().take_damage(damage=damage)


class VampireKing(Vampire):
    def __init__(self, name):
        # super().__init__(name=name, hit_points=140, number_of_lives=2)  # wont work because the Vampire Class constructor
        #                                                                 # doesn't number_of_lives
        super().__init__(name, hit_points=140)
        # self.hitPoints = 140
        self._lives = 2


enem = Enemy("enem", 20, 2 )
lives = enem.lives

# while lives > 0:
#     enem.take_damage(5)
#     lives = enem.lives
#     print(lives)
#     time.sleep(1)

# troll = Troll("Urg")
# troll.grunt()
# print(troll.lives)
#
# while troll.lives > 0:
#     troll.take_damage(6)

vamp = VampireKing("Vamp")

while vamp.lives > 0:
    vamp.take_damage(20)
