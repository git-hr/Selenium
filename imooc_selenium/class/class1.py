class Test():
    a = 0
    b = 0
    c = 0
    def __init__(self, a):
        self.a = a
        self.b = a + 1
        print(self.a,self.b)
    
    def printa(self):
        print(self.a,self.b)

    @classmethod
    def classfunc1(cls):
        cls.c += 1
        print(cls.c)