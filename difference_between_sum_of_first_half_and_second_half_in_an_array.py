N=int(input())
l=list(map(int,input().split()))
if N%2==0:
    pass
else:
    l.append(l[-1]+1)
fh=sh=0
for i in range(0,(N+1)//2):
    fh+=l[i]
for j in range((N+1)//2,len(l)):
    sh+=l[j]
print(abs(fh-sh))
    