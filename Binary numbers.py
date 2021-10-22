n = int(input())
a = list(bin(n))
a = a[2:]

c = 0
max = 0
for i in range(len(a)):
    if a[i] == '1':
        c +=1
    else:
        if max < c:
            max = c
        c= 0 

if max < c:
    print(c)
else:
    print(max)