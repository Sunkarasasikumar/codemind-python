def mis(l):
    j=1
    while True:
        if j not in l:
            return j
        j+=1
n=int(input())
l=list(map(int,input().split()))
print(mis(l))
    