n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
count=0
for i in range(len(l)):
    if l[i]%2==1:
        count+=1
print(count)