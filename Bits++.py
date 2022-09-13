n=int(input())
x=0
for i in range(n):
    op=input()
    if op.startswith('+') or op.endswith('+'):
        x+=1
    elif op.startswith('-') or op.endswith('-'):
        x-=1
print(x)
    