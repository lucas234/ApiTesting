

class A(object):
    def __init__(self):
        pass

    def test(self):
        print 1

    @staticmethod
    def test2():
        print 2

    @classmethod
    def test3(cls):
        print 3

class B(A):

    def test4(self):
        print 123

class C(B,A):
    pass

c = C()
a = A()
b = B()
a.test()
a.test3()
B.test2()
c.test()
print a.test
print A.test
print a.test2
print A.test2
print a.test3
print A.test3