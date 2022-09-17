
a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    f=0
    while n:
        r=n%10
        if r==0 or i%r!=0:
            f=1
            break
        n=n//10
    if f==0:
        print(i,end=" ")