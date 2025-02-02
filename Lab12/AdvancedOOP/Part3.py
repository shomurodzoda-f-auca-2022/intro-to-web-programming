class Bird(object):
    @staticmethod
    def fly():
        print("Bird fly")

class Airplane(Bird):
    @staticmethod
    def fly():
        print("Airplane fly")

class Fish(Bird):
     @staticmethod
     def fly():
        print("Fish fly")

for obj in (Airplane, Bird, Fish):
    obj.fly()