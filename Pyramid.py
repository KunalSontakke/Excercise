
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
*
* *
* * *
* * * *
* * * * *
# """
# for i in range(0,6):
#     for j in range(1,i+1):
#         print(" *",end=" ")
#     print()


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
for i in range(1,6):
    print(" " * (6-i) + "* " * i)


"""
* * * * *
* * * *
* * *
* *
*
"""


for i in range(1,6):
    for j in range(1,i+1):
        print(" *" * (j) + " " * (6-i))
    print()
"""

    *
   * *
  * * *
 * * * *
* * * * *
"""


