"""
1) Difference between tuple and string
2) difference between selenium and pytest
3) difference between driver.close() and driver.quit()
4) markers in pytest
5) pull requests in git
6) is Agile incremental or iterative
7) Defect Life cycle

"""
"""combine both dictionaries into a dictionary"""
dic1 = {"name":"kunal","lastname":"sontakke","company":"calsoft","location":"indore"}
dic2 = {"language":"python","framework":"pytest","SCM":"git"}

dic3 = {}
dic3.update({**dic1,**dic2})
print(dic3)


"""create a function while find HCF of two numbers"""


def find_HCF(n1, n2):
    min_num = min(n1,n2)
    hcf = 1
    for i in range(1,min_num+1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
    print(f"hcf of {n1} and {n2} is {hcf}")


n1 = int(input("n1:"))
n2 = int(input("n2:"))

find_HCF(n1,n2)
