"""Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)."""
import re
def find_char(string : str) -> bool:
    chaRe = re.compile(r'[^a-zA-Z0-9]')
    string = chaRe.search(string)
    return bool(string)

print(find_char('!@#$%^&*()-+'))


"""Write a Python program that matches a string that has an a followed by zero or more b's."""

def text_match(str1 : str) -> None:
    pattern = '^a(b)*$'
    charSet = re.search(pattern,str1)
    if charSet:
        print("Match found")

    else:
        print("No Match found")

text_match("ab")

"""Write a Python program that matches a string that has an a followed by one or more b's.

"""
def text_match_2(str1 : str) -> None:
    pattern = '^a(b+)$'
    charset= re.search(pattern,str1)
    if charset:
        print("Match Found")
    else:
        print("No Match Found")

text_match_2("ab")

# =========================================================

"""Write a Python program that matches a string that has an a followed by three 'b'."""
def text_match_3(str1 : str) -> None:
    pattern = '^(a)*b{3}'
    charset = re.search(pattern,str1)
    if charset:
        print('Match Found')
    else:
        print('No Match Found')

text_match_3('aaaabbb')

# =========================================================================
"""Write a Python program that matches a string that has an a followed by two to three 'b'."""

def text_match_4(str1 : str) -> None:
    pattern = '^ab{2,3}'
    charset = re.search(pattern,str1)
    if charset:
        print("Match Found")
    else:
        print("No Match Found")

text_match_4('abbb')

# ==================================================================================

""""Write a Python program to find sequences of lowercase letters joined by an underscore."""

def text_match_5(str1 : str) -> None:
    pattern = '^[a-z]+_[a-z]+$'
    charset = re.search(pattern,str1)
    if charset:
        print("Match Found")
    else:
        print("No Match Found")

text_match_5('abbbb_abbb')

# ==============================================================================
"""Write a Python program to find the sequences of one upper case letter followed by lower case letters."""

def match_UpperCase_lowercase(str1 : str ) -> None:
    pattern = '[A-Z]+[a-z]+$'
    charset = re.search(pattern,str1)
    if charset:
        print("Match Found")
    else:
        print("No Match Found")
match_UpperCase_lowercase('PyThOn')