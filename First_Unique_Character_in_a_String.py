n=input()
for i in range(len(n)):
    if n[i] not in n[:i]+n[i+1:]:
        print(i)
        break
else:
    print(-1)
    