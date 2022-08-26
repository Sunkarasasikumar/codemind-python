n=int(input())
l=list(map(int,input().split()))
k=int(input())
#print(l)
a=[]
for i in range(len(l)):
    if l.count(l[i])==k:
        a.append(l[i])
a=set(a)
if len(a)==0:
    print(-1)
else:
    for i in a:
        print(i,end=" ")
        