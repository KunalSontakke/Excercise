"""Check if a String Contains Only Unique Characters

Input = "abcdef" # Output: True
Input = "hello"  # Output: False
"""
# string = "abcdef"
def check_unique_character(string):
    for i in string:
        if string.count(i) >1:
            return False
    else:
        return True

print(check_unique_character("abcdef"))
# ==================================================================

"""Write a program for the below strings. 

Reference Input & Output
- Input = Alexa  --->  output = A Al Ale Alex Alexa
- Input = abc  --->  output = a ab abc
- Input = a --->  output= a"""

def check_string(string):
    out = ""
    for i in range(len(string)):
        out += string[:i+1]
    print(out)
check_string("Alexa")

# ==============================================================
"""Find the Longest Word in a String

Input: The quick brown fox jumped over the lazy dog
Output: jumped"""

def find_longest_word(string):
    return "".join([i for i in string.split() if len(i) == max(len(word)for word in string.split())])

inp = "The quick brown fox jumped over the lazy dog"
print(find_longest_word(inp))

