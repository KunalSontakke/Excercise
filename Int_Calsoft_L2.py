
inp = "my name is kunal"
op = "kunal is name my"

inp_spl = inp.split()
rev_inp = inp_spl[::-1]
out = " ".join(rev_inp)
print(out)

lst = [22,23,12,34,56,67,90,78]

# output = [90,78,22,23,12,34,56,67]

lst = lst[-2:] + lst[:-2]
print(lst)

