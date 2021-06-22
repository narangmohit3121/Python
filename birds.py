class Duck(object):
    def walk(self):
        print("Duck walking")

    def fly(self):
        print("Into the sky")


class Penguin(object):
    def walk(self):
        print(type(self).__name__, "walking")


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck):
        self.flock.append(duck)

    def migrate_flock(self):
        problem = None
        for bird in self.flock:
            # print(type(bird) is Duck)
            # print(isinstance(bird, Duck)):
            # if isinstance(bird, Duck):
            #     bird.fly()
            try:
                bird.fly()
            except BaseException as e:
                problem = e
        if problem:
            raise problem


class Mallard(Duck):
    pass


duck1 = Duck()
duck2 = Duck()
duck3 = Duck()
duck4 = Duck()
duck5 = Duck()
duck6 = Duck()
duck7 = Penguin()
duck8 = Mallard()

flock = Flock()
flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)
flock.add_duck(duck8)

flock.migrate_flock()
