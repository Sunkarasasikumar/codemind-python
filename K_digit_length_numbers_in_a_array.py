def ele_len(n):
    return len(str(n))
N,K=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in l:
    if ele_len(abs(i)) == K:
        count+=1
print(count)
