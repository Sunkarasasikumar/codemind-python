n=int(input())
l=list(map(int,input().split()))
count=0
min=max=-1
for i in range(n):
    if l[i]%2==0:
        min=i
        break
for i in range(n-1,-1,-1):
    if l[i]%2==0:
        max=i
        break
for i in range(min+1,max):
    if l[i]%2==1:
        count+=1
print(count)