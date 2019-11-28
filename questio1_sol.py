class MyException(Exception):
    def __init__(self,k):
        self.k = k
    def __str__(self):
        return str(self,k)
def xyz(a,b):
    c = a+b
    if c < 150:
        raise MyException('custom exception occured')
    else:
        return c
a = int(input())
b = int(input())
print(xyz(a,b))