input = "zzzbbbccczzssdd"
output = "Z3b3c3z2s2d2"
out = ''
count = 1
for i in range(len(input) - 1):
    if inp[i] == inp[i + 1]:
        count += 1

    else:
        out += inp[i - 1] + str(count)
        count = 1

out += input[-1] + str(count)
print(out)


"""
* * * * * * *
 * * * * * *
   * * * *
    * * *
     * *
      *
"""