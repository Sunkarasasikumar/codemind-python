n=int(input())
l=list(map(int,input().split()))
s=set()
for i in range(len(l)):
    if l[i]==l.count(l[i]):
        s.add(l[i])
if len(s):
    print(min(s),max(s))
else:
    print("-1")
        