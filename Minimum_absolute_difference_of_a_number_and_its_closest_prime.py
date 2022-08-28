def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True 
n=int(input())
f=0
if is_prime(n):
    print(0)
else:
    n1=n2=n
    while True:
        if n1==1:
            f=1
            break
        n1-=1
        if is_prime(n1):
            break
    while True:
        n2+=1
        if is_prime(n2):
            break
    if abs(n1-n)<=abs(n2-n) and f==0:
        print(abs(n1-n))
    else:
        print(abs(n2-n))
        
    
        
            