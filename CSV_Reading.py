"""Read each row from a given csv file and print a list of strings"""
import csv

# with open('Data/departments.csv',newline='') as file:
#     data = csv.reader(file,delimiter=",",quotechar="|")
#     for row in data:
#         print(",".join(row))

# =============================================================================================

"""Write a Python program to read a given CSV file having tab delimiter."""

# with open('Data/countries.csv',newline='') as file:
#     data = csv.reader(file,delimiter="\t")
#     for row in data:
#         print(",".join(row))

# ============================================================================================
"""Write a Python program to read a given CSV file as a list."""
# with open("Data/employees.csv","r",newline='') as file:
#     data = csv.reader(file)
#     data_list = list(data)
# print(data_list)

# ==============================================================================
"""Write a Python program to read a given CSV file as a dictionary."""
dict_reader = csv.DictReader(open('Data/departments.csv','r',encoding="utf-8"))
for row in dict_reader:
    print(row)
