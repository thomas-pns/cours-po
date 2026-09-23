import numpy as np

class polynome:
    def __init__(self, a, b, c):
        self.__a= a
        self.__b = b
        self.__c = c
    def evaluation(self, x):
        return self.__a*x**2+self.__b*x+self.__c

    def racines(self):
        self.delta=self.__b**2-4*self.__a*self.__c
        print(self.delta)
        if self.delta<0:
            return "débrouille toi"
        elif self.delta==0:
            return -self.__b/(2*self.__a)
        else:
            return (-(self.__b+np.sqrt(self.delta))/(2*self.__a), -(self.__b-np.sqrt(self.delta))/(2*self.__a))
 
    def get_a(self):
        return self.__a
    def get_b(self):
            return self.__b
    def get_c(self):
            return self.__c
    
    def add(self, p2):
        return polynome(self.__a+p2.get_a(),self.__b+p2.get_b(),self.__c+p2.get_c())

    def subtract(self, p2):
        return polynome(self.__a-p2.get_a(),self.__b-p2.get_b(),self.__c-p2.get_c())

    def multiply(self, s):
        return polynome(s*self.__a, s*self.__b, s*self.__c)
    
    def show(self):
        return f"{self.__a}x^2+{self.__b}x+{self.__c}"
