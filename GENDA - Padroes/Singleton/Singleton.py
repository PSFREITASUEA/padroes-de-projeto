import random
import hashlib


class Singleton(object):
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls.hash = ""
            cls.int = 1
        return cls.instances[cls]


class MyClass(Singleton):

    def GiveEachInstanceAUniqueValue(self):
        self.int = 2
        hashVar = random.randint(0, 1000)
        hashObj = hashlib.sha1(b'%d' % hashVar)
        hex_dig = hashObj.hexdigest()
        return hex_dig

    def __init__(self):
        if self.int == 1:
            self.hash = str(self.GiveEachInstanceAUniqueValue())
            print(self.hash)


a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()

if id(a) == id(b) == id(c) == id(d):
    print(a.hash)
    print(b.hash)
    print(c.hash)
    print(d.hash)

