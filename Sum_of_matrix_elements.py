M=int(input())
N=int(input())
c=[]
for i in range(M):
    r=list(map(int,input().split()))
    c.extend(r)
print(sum(c))