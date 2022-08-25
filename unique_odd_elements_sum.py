N=int(input())
L=list(map(int,input().split()))
s=set(L)
sum=0
for i in s:
    if i%2==1:
        sum+=i
print(sum)