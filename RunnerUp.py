#Find the Runner Up Score!
#By: Wilson Aballey

#First solution
n = int(input())
arr = input().split()
print (sorted(set(arr))[-2])


#Second Solution. Uncomment before running.
'''
n = int(input())
arr = input().split()
m = list(set(arr))
b = m.remove(max(m))
print(max(m))
'''