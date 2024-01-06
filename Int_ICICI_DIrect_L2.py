"""
1) Structure of project
2) Dynamic Xpath( starts-with,ends-with)
3) HTML
"""

"""python program to display Maximum frequency character in String"""


def max_freq_char(ip_str):

    freq = {}

    for i in ip_str:
        if i in freq:
          freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    max_char = max(freq,key=freq.get)
    return max_char


ip_str = input("Enter string : ")
print(max_freq_char(ip_str))


