n=input()
l=[]
for i in n:
    if i=='a' or i=='e' or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i=="E"  or i=="U":
        if i not in l:
            l.append(i)
for i in l:
    print(i,end=" ")
        
        