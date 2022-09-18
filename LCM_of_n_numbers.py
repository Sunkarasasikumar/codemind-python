n=int(input())
arr=list(map(int, input().split()))
lcm=max(arr)
while True:
    f=0
    for i in arr:
        if lcm%i!=0:
            f=1
            break
    if f!=1:
        print(lcm)
        break
    lcm+=1
    