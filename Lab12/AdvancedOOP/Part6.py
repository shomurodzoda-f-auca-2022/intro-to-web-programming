class A:
    @staticmethod
    def methodA():
        print("Method A")

class B:
    @staticmethod
    def methodB():
        print("Method B")

class C(A, B):
    pass

c = C()
c.methodA()
c.methodB()