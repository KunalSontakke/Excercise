"""data = [
{'A':10},
{'B':20},
{'A':20},
{'B':30},
{'A':35},
{'C':30}]
output = [{'A':[10,20.35],'B':[20,30],'C':[30]}]
"""
data = [
{'A':10},
{'B':20},
{'A':20},
{'B':30},
{'A':35},
{'C':30}]
out = {}
for d in data:
    for category,value in d.items():
       if category not in out:
           out[category] = [value]
       else:
            out[category].append(value)
print(out)

"""WAP to find Prime numbers from range 30 to 40"""
