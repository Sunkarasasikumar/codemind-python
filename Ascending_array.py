def desc(a):
    for i in range(len(a)-1):
        if a[i]>=a[i+1]:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
print("yes" if desc(l) else "no")