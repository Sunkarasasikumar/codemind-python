def is_palin(i):
    if i==i[::-1]:
        return True
    return False
n=input()
n=n.lower()
print(is_palin(n))