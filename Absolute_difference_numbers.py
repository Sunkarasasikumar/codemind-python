n,x=map(int,input().split())
div=pow(10,x)
last=n%div
first=int(str(n)[:x])
print(last-first if last>first else first-last)