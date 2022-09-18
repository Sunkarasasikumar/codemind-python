T=int(input())
for i in range(T):
    n=input()
    for j in n:
        if j.isdigit()==False:
            print(False)
            break
    else:
        print(True)   