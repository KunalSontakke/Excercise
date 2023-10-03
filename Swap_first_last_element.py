# # How to swap first and last elements in the list

def swap_list(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]
    return newlist


newlist = [12, 43, 56, 78, 23]

print(swap_list(newlist))


