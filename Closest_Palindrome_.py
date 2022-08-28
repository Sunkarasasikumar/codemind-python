def is_palin(n):
    if n==int(str(n)[::-1]):
        return True
    return False
n=int(input())
n1=n2=n
while True:
    n1=n1-1
    if is_palin(n1):
        a=n1
        break
while True:
    n2=n2+1
    if is_palin(n2):
        b=n2
        break
if abs(n2-n)<abs(n1-n):
    print(n2)
elif abs(n2-n)==abs(n1-n):
    print(n1,n2)
else:
    print(n1)
    