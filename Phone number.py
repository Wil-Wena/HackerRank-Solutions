
m = int(input())
b= {}
for i in range(m):
    text = input().split()
    b[text[0]] = text[1]
#print(b)
while True:
    try:
        c = input()
        if c in b:
            v = b[c]
            print(c +"="+ v)
        else:
            print('Not found')
    except EOFError:
        break




