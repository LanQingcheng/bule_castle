# -*- coding: utf-8 -*-

#斐波那契数列-list
'''
def fab1(max):
                n, a, b = 0, 0, 1
                L = list()
                while n < max:
                                L.append(b)
                                a, b = b, a+b
                                n+=1
                return L
'''
#斐波那契-iterable
'''
class Fab(object):
                def __init__(self, max):
                                self.max = max
                                self.n, self.a, self.b = 0, 0, 1

                def __iter__(self):
                                return self

                def next(self):
                                if self.n < self.max:
                                               r = self.b
                                               self.a, self.b = self.b, self.b+self.a
                                               self.n+=1
                                               return r
                                raise StopIteration()

fab = Fab(5)
for i in fab:
                print i
'''
#斐波那契-yield
'''
def fab2(max):
                n, a, b = 0, 0, 1
                while n < max:
                                yield b
                                a, b = b, a+b
                                n+=1
f = fab2(5)
print(f.next())
'''
#杨辉三角
def triangle():
                L = [1]
                while True:
                                yield L
                                L.append(0)
                                #print(len(L))
                                L = [L[i-1] + L[i] for i in range(len(L))]

n = 0
for t in triangle():
                print(t)
                n+=1
                if n == 5:
                                break
