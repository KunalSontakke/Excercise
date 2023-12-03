dic ={
    "Students": {
        "name": " QA Tester 2",
        "Marks": {
            "maths": 10,
            "English": 11
        }
    },
    "Students1": {
        "name": " QATester1",
        "Marks": {
            "maths": 30,
            "English": 35
        }
    }
}
"""print student name whose 'maths' marks more than 20"""
# if dic["Students"]["Marks"]["maths"] > dic["Students1"]["Marks"]["maths"]:
#     print(dic["Students"]["name"])

# else:
#     print(dic["Students1"]["name"])
# or
for student_key,student_value in dic.items():
    if student_value["Marks"]["maths"] > 20:
        print(student_value["name"])

# # =============================================
dic2 ={
    "Students": {
        "name": " QATester 2",
        "Marks": {
            "maths": 10,
            "English": 11
        }
    },
    "Students1": {
        "name": " QATester 1",
        "Marks": {
            "maths": 30,
            "English": 35
        }
    },
    "Students3": {
        "name": " QATester 4",
        "Marks": {
            "maths": 30,
            "English": 35
        }
    }
}
max_marks = float('-inf')
topper = ""
for student_key,student_value in dic2.items():
    maths_marks = student_value["Marks"]["maths"]
    if maths_marks > max_marks:
        max_marks = maths_marks
        topper += student_value["name"]
    elif maths_marks == max_marks:
        topper += student_value["name"]

print("topper of maths is",topper)

# ==============================================================
#
# lis = [1,2,3,4,5,6,7,45,67,24,21,69]
# op = [3,4,5,6,7,45,67]
# print(lis[2:-3])

