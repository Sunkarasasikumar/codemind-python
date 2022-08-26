n=int(input())
l=list(map(int,input().split()))
#print(l)
a=[]
for i in range(len(l)):
    if l.count(l[i])==l[i]:
        a.append(l[i])
a=set(a)
if len(a)==0:
    print(-1)
else:
    s=sum(a)/len(a)
    print("{:.2f}".format(s))
        
        