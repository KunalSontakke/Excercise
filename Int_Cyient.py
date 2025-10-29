""""WAP for reverse string"""
# inp = "kunal"
# out = inp[::-1]
# print(out)

# out = ""
# for i in inp:
#     out = i + out
# print(out)

inp1 = "k1u2n3a4l5"
letter = []
num = []
for i in inp1:
    if i.isalpha():
        letter.append(i)
    else:
        num.append(i)
print("".join(letter))
print("".join(num))

"""students = {
    "S0001": {
        "name": "Bluee",
        "subjects": {
            "Math": 88,
            "Physics": 92,
            "Chemistry": 85,
        },
            "S0002": {
        "name": "Bluee",
        "subjects": {
            "Math": 88,
            "Physics": 92,
            "Chemistry": 85,
        }
    },
output should be : {'S001': 88.33, 'S002': 85.6}

"""
students = {
    "S0001": {
        "name": "Bluee",
        "subjects": {
            "Math": 88,
            "Physics": 92,
            "Chemistry": 85,
        },
    },
    "S0002": {
        "name": "Kunal",
        "subjects": {
            "Math": 90,
            "Physics": 92,
            "Chemistry": 75,
        },
    },
}
average_marks = {}

for student_id, info in students.items():
    subjects = info["subjects"]
    avg = sum(subjects.values()) / len(subjects)
    average_marks[student_id] = round(avg, 2)

print(average_marks)
