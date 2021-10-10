#Collections problem
from collections import Counter
n = int(input("No. of shoes available"))
m = list(map(int,input().split(" "))) # Shoe sizes available
#print(m)
x = Counter(m)
b = int(input("No. of customers"))

c= 0
for i in range(b):
    size,price = map(int,input().split())

    if x[size]:
        x[size] -=1
        c = c + price
print(c)