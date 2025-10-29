"""
1) Sprint Ceremonies
2) Priority and Severity
3) High Priority and low Severity
4) High Severity and low Priority
5) Defect Lie Cycle
6) what suggestions given in Sprint meetings
"""

# =================================================================================================
from collections import Counter
#
"""Display the duplicate letters in string and print the occurrence of the letters"""
input = "mississipi"

freq = {}
for i in input:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

for letter,count in freq.items():
    if count > 1:
        print(letter,":",count)


# ==================================================================================================
#
string = "I am from Maharashtra"
output = "I ma morf arthsarahaM"

b = string.split()
print(b)
for i in b:
    print(i[::-1], end=" ")


# # ===================================================================================================
#
# """SQL Queries"""""
#
# select Employee.emp_name, Salary.salary from employee inner join salary on employee.emp_id = salary.emp_id where
# Salary.salary = (select max(salary) from Salary);
#
# # select case(when 1=1 then 'Y' else 'N' end) from tableName;



