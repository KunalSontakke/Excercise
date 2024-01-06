str = "vivek"

freq = {}

for i in str:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)

print(max(freq.items(),key= lambda x: x[1]))


def func():
    pass

func()
