def ele_len(n):
    return len(str(n))
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        print(ele_len(abs(i)),end=" ")
    else:
        print(ele_len(i),end=" ")
        