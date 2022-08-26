def is_palindrome(n):
    if len(str(n))==l:
        return True
    else:
        n=str(n)
        rev=n[::-1]
        if n==rev:
            return True
        return False
n=int(input())
l=list(map(int,input().split()))
count=0
for i in l:
    if is_palindrome(i):
        count+=1
print(count)
        