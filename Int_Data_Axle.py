""""
1. Framework Structure
2. difference between class and object
3. Public, Protected and Private Specifier
4. difference between driver.close() and driver.quit
5. How can we write/find xpath

"""
"""count the frequency of each letter regardless of it's case"""

inp = "Th1s !s @ pyThon Interv13w"

# freq = {}
# low_case = inp.lower()
# for i in low_case:
#     if i.isalnum():
#         if i not in freq:
#             freq[i] = 1
#         else:
#             freq[i] += 1
# print(freq)

# ======================================================================================================================
input_str = "Th1s !s @ pyThon Interv13w"
out = "tH1S 2S 3 PYtHON iNTERV45W"


def convert_string(input_str):
    frequency = {}
    output_str = ''

    for char in input_str:
        if char.isalpha():
            if char.islower():
                output_str += char.upper()
            else:
                output_str += char.lower()

        elif char == " ":
            output_str += " "

        elif char.isdigit():
            digit_count = frequency.get('digits', 0) + 1
            frequency['digits'] = digit_count
            output_str += str(digit_count)

        else:
            special_count = frequency.get('specials', 1) + 1
            frequency['specials'] = special_count
            output_str += str(special_count)


    return output_str

input_str = "Th1s !s @ pyThon Interv13w"
output = convert_string(input_str)
out = "tH1S 2S 3 PYtHON iNTERV45W"

print(input_str)
print(out)
print(output)


