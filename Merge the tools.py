#Merge the Tools Solution!
# It prints each subsequence on a new line. There will be (length of string/ length of each substring) of them.
# No return value is expected.

#By:Wilson Aballey



string, k = input(), int(input())

def merge_the_tools(string, k):
    while string:
        s = string[0:k] #String index 
        seen = ''
        for c in s:
            if c not in seen:
                seen += c  #Appends each letter
        print(seen)
        string = string[k:] #Sets string to the current index not printe out.

#Function call
merge_the_tools(string, k)