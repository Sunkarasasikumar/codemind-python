n1=input()
n2=input()
n1,n2=n1.lower(),n2.lower()
f=0
if len(n1)==len(n2):
    for i in n1:
        if i in n2:
            continue
        else:
            break
            f=1
    if f:
        print(False)
    else:
        print(True)
else:
    print(False)
            
        