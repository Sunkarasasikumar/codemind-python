N=int(input())
L=list(map(int,input().split()))
s=set(L)
sum=0
for i in s:
    if i%2==0:
        sum+=1
print(sum)