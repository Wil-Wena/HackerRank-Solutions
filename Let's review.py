

#So here it prints the odd and even indices. Index 0 is considered even.
#The user inputs the index he wants and then it prints
#  all odd or even letters on the same line with a space in between

m = int(input())  # User input should be an integer.

for i in range(m): 
    s=input(); # The word the user wants to print the odd or even indices.
    print(*["".join(s[::2]),"".join(s[1::2])]) #Unpacks and prints the letters.