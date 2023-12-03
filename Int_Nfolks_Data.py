# """write a python program to create a list of  prime numbers between range from 1 to user-defined input."""
# num = int(input("Enter the number"))
# prime_nos = []
# for i in range(2,num):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         prime_nos.append(i)
# print(prime_nos)
#
# # ======================================================================================================================
#
# """write a python program to find leap years between a range
# ex .
# enter starting year : 1890
# enter ending year : 1910
# leap year :
# 1892
# 1896
# 1900
# 1904
# 1908
#
# """
# start_year = int(input("Enter the starting year : "))
# end_year = int(input("Enter the starting year : "))
# for year in range(start_year,end_year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(year)
#
#
# # =====================================================================================================================
# """
# write a python program to separate odd and even index elements of string into two different lists.
# string = "JOHN DOE 123"
# even_lists = ['J','H',' ','O',' ','2']
# odd_lists = ['O','N','D','E','1','3']
# """
# string = "JOHN DOE 123"
# even_list = [string[i] for i in range(len(string)) if i % 2 ==0]
# odd_list = [string[i] for i in range(len(string)) if i % 2 ==1]
#
# print(even_list)
# print(odd_list)

# ======================================================================================================================
"""write a python program to convert scores into degrees for pie chart
Test Case 1 : 
Enter the total subjects : 3 
Enter label for the subject1 : study
Enter the value for study : 4
Enter the label for subject2 : office
Enter the label for office : 8
Enter the label for subject3 : others
Enter the value for others : 12

Output:
study : 60
office : 120
others : 180

Test case 2:
Enter the total subjects : 4 
Enter label for the subject1 : study
Enter the value for study : 4
Enter the label for subject2 : office
Enter the value for office : 8
Enter the label for subject3 : others
Enter the  value for others :12
Enter the label for subject4 : play
Enter the value for play : 15

Output:
study : 60
office : 120
others : 180
play : 180

# """
dic = {}
total_subjects = int(input("Enter the total subjects :"))
for i in range(1,total_subjects+1):
    subject = input(f"Enter the label for subject{i} : ")
    value = int(input(f"Enter the value for {subject} :"))
    dic[subject] = value

for subject,value in dic.items():
    print(f"{subject}:{value * 15}")

