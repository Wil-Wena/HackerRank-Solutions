#Maximize it solution
#Wilson Aballey
from itertools import product
from math import pow
it = list(map(int,input().split()))
a , b = it[0],it[1]
listings=[]

for i in range(a):
    listings.append(list(map(int,input().split()))[1:])

M = list(product(*listings))
final_answer =[]
for i in M:
    sum = 0
    for j in i:
        sum = sum + pow(j,2)
    final_answer.append(sum % b)
print(max(final_answer))
