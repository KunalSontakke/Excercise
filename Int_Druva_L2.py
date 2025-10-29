"""Input = [10,3,6,7,4,7,2,12,9,7]
Output = [[10],[3,6,7],[4,7],[2,12],[9],[7]]
"""
input = [10,3,6,7,4,7,2,12,9,7]
out = []
current_group = [input[0]]

for i in range(1,len(input)):
    if input[i] > input[i-1]:
        current_group.append(input[i])
    else:
        out.append(current_group)
        current_group = [input[i]]
out.append(current_group)
print(out)


"""Write a program which will take a word as console input. The program is required to chop 1 character from the input word,
alternatively from the left and the right ends of the word, and display the chopped word at every step.
The chopping should start from the right end of the word (the last character). First, the original form of the word is to be shown, 
and then the chopped words. The chopping should continue until only one character of the word remains.

For example:
If the word COMBINATION is supplied as input to the program, then the output of the program will be:

COMBINATION
COMBINATIO
OMBINATIO
OMBINATI
MBINATI
MBINAT
BINAT
BINA
INA
IN
N
"""

inp = "COMBINATION"
chop_from_right = True

while len(inp) > 1:
    if chop_from_right:
        inp = inp[:-1]
    else:
        inp = inp[1:]

    print(inp)
    chop_from_right = not chop_from_right

"""get - id 
get - without params = Will give you all records (default page size is 100)
get - limit (and/or) offset , limit default value is 100 and maximum is 500, offset default value is 0"""


"""Test cases 
1) request GET should sent successfully for fetching value "id"
2) Response status status code should be 200
3) without using params GET request should fetch maximum records
4)if any params for pagination is given then same number of records should be displayed
5)if "offset" params is given then records should be started from this param value else records should be started from "0"
6)if "limit" params is given by user then same number of records should be displayed else default number of records should be 100
 
"""

