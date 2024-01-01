"""
1) Automated Framework

Explaining your testing framework in a project involves effectively communicating its purpose, structure, components,
and how it facilitates testing activities within the project.
1. Understand Your Audience:

    Know Your Audience: Understand the technical expertise and familiarity of your audience with testing frameworks.
    Tailor your explanation accordingly, avoiding technical jargon if the audience is non-technical.

2. Define the Testing Framework:

    Purpose and Objective: Explain the primary purpose of the testing framework. Highlight how it aids in organizing, structuring, and executing tests efficiently.
    Components and Structure: Describe the various components, modules, or layers within the testing framework (e.g., test scripts, libraries, utilities).
    Supported Testing Types: Mention the types of testing supported by the framework (e.g., unit testing, integration testing, functional testing).

3. Highlight Key Features:

    Automation Capabilities: Explain how the framework supports test automation and its ability to reduce manual effort.
    Scalability and Reliability: Emphasize the scalability and re-usability of test scripts or components within the framework across different modules or projects.
    Reporting and Analysis: Discuss the framework's reporting capabilities and how it facilitates result analysis and defect tracking.

4. Framework Implementation:

    Integration with Tools: Explain how the framework integrates with other tools or technologies used in the project (e.g., version control, CI/CD pipelines).
    Adherence to Standards: Mention if the framework follows industry standards, best practices, or specific coding conventions.

5. Benefits and Impact:

    Efficiency and Time Savings: Illustrate how the framework contributes to faster test execution, reduced effort, and increased productivity.
    Improved Quality: Emphasize how the framework aids in achieving higher test coverage and better quality assurance.

6. Real-life Examples or Case Studies:

    Demonstration or Examples: Use real-life examples, case studies, or demonstrations to showcase the framework's effectiveness in action.
    Success Stories: Share success stories or instances where the framework positively impacted testing outcomes or project deliverables.

7. Address Questions and Feedback:

    Encourage Interaction: Encourage questions and feedback from your audience to ensure they have a clear understanding of the framework's functioning and relevance to the project.
    Clarify Doubts: Address any concerns or doubts raised by the audience to provide a comprehensive explanation.

8. Conclusion and Follow-up:

    Summary: Summarize the key points discussed and reiterate the significance of the testing framework in the project's success.
    Follow-up Resources: Provide additional resources or documentation for further reference or in-depth understanding.
"""
"""
2) Dynamic Language
3) difference between .py and .pyc

"""

""" Write python program to find fibonacci series"""

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# # Driver Program


print(Fibonacci(10))
#  =========================================================================================================================

"""write python program to find vowels in string"""


def printVowels(string):
    # to print the vowels
    for i in string:
        if i in "aeiouAEIOU":
            print(i, end=',')


# take input
string = input('Enter any string: ')

# calling function
printVowels(string)

# =============================================================================================================================

""" Write a Python Program to Convert Comma Separated List to a String.
favorite_prog = ["Python", "SQL", "GO"]
Python, SQL, GO """

fav_prog = ["Python", "SQL", "GO"]

fav_prog = ",".join(fav_prog)

print(fav_prog)

names = "hat"
change = names.replace("h", "b")
print(names)





