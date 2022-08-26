n=input()
count=0
for i in n:
    if i.isalnum() or  i.isspace():
        continue
    else:
        count+=1
print(count)