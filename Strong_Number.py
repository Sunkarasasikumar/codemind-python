def factorial(num):
    if num<2:
        return 1
    pro=1
    for i in range(1,num+1):
        pro*=i
    return pro
n=int(input());sum=0
for i in str(n):
    sum+=factorial(int(i))
if sum==n:
      print('The number',n,'is a strong number')
else:
      print('The number',n,'is not a strong number')