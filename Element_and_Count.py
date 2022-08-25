N=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if l[i] in s:
        continue
    else:
        s.append(l[i])
        print(l[i],end=" ")
        print(l.count(l[i]),end=" ")
