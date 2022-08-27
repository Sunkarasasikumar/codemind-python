i=input()
n=list(i)
if n.count('9')==len(n):
    print(i)
else:
    a=n.index('6')
    n[a]='9'
    print("".join(n))