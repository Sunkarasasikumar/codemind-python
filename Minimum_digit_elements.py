def ele_len(n):
    return len(str(n))
N=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
    lis.append(ele_len(i))
n=min(lis)
print(lis.count(n))
    
        
