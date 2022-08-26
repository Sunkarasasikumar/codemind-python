def ele_len(n):
    return len(str(n))
N=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
    lis.append(ele_len(abs(i)))
n=max(lis)
for i in l:
    if len(str(abs(i)))==n:
        print(i,end=" ")
    
        
