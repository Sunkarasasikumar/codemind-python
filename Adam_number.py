n=int(input())
nn=n*n
r=int(str(n)[::-1])
rr=r**2
if n%10==0:
    print(False)
elif rr==int(str(nn)[::-1]):
    print(True)
else:
    print(False)