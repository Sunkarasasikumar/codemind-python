def can_made(a,b):
    for i in a:
       if a.count(i)>b.count(i):
           return False
    return True
       
a,b=input().split()
print(can_made(a,b))