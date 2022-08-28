n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if l.count(i)==i and i not in m:
        m.append(i)
if len(m)>0:
    print(len(m))
else:
    print(0)