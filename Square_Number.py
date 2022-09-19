import math
n=int(input())
def fun(n):
    for i in range(int(math.sqrt(n))+1):
        for j in range(int(math.sqrt(n)),-1,-1):
            if i==j:
                continue
            elif i*i+j*j==n:
                return True
    return False
print(fun(n))
