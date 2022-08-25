N=int(input())
l=list(map(int,input().split()))
if N%2==0:
    pass
else:
    l.append(0)

for i in range(len(l)):
    print(l[i],end=" ")
