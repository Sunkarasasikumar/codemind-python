def pretty(n):
    last=int(str(n)[-1])
    if last==2 or last==3 or last==9:
        return True
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count=0
    for i in range(a,b+1):
        if pretty(i):
            count+=1
    print(count)