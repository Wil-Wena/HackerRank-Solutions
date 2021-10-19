#Arrays.
#Prints the user input list from backwards

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
if n == len(arr):
    print(*arr[::-1],'')
else:
    print('Invalid input try again next time.')
