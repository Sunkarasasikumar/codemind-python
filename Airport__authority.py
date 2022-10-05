N=int(input())
l=list()
for i in range(N):
    l.append(int(input()))
t=int(input())
def weight_machine(N,l,t):
    cost=0
    for i in l:
        if i>t:
            cost+=2
        else:
            cost+=1
    return cost
print(weight_machine(N,l,t))