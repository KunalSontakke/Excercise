"""count the frequency of each letter regardless of it's case"""

inp = "Th1s !s @ pyThon Interv13w"
out = {}
for char in inp.lower():
    if char not in out:
        out[char] = 1
    else:
        out[char] += 1
print(out)

input_str = "Th1s !s @ pyThon Interv13w"
out = "tH1S 2S 3 PYtHON iNTERV45W"

print("".join([i.lower() if i.isupper() else i.upper() for i in input_str]))
