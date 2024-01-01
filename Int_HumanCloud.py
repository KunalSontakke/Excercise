"""
1) pytest framework
2) Project Info
3) Suppose Bug is reproduced in Production environment
4) Story point
5) Sprint Framework Ceremonies
6) New changes introduced in project

    Assess the Impact: Evaluate the impact of the new changes on the current sprint goals and commitments.
    Determine if the changes are critical and align with the sprint objectives.
    Consider the potential benefits versus the disruption they might cause.

    Prioritization: If the new changes are deemed necessary for the sprint, prioritize them alongside the existing sprint backlog items.
    Discuss with the team to understand the importance and urgency of the changes compared to the existing work.

    Collaboration and Team Discussion: Hold discussions with the development team, Scrum Master, and stakeholders to collectively decide on how to handle the new changes.
    This discussion should include potential impacts on existing sprint goals, workload, and achievable outcomes.

    Adjusting the Sprint Backlog: If the new changes are accommodated, reevaluate the sprint backlog.
    Adjust priorities and tasks as needed, considering the team's capacity and the sprint duration.

    Communication: Transparent and clear communication is vital. Inform stakeholders, team members, and affected parties about the introduction of new changes.
    Clearly articulate how these changes will impact the current sprint and set realistic expectations.

    Adaptation and Flexibility: Embrace Agile principles of adaptability. Agile methodologies encourage responding to change over rigidly following a plan.
    If new changes are necessary and aligned with project goals, adapt the sprint plan accordingly.

    Mitigating Risks: Identify any risks associated with introducing new changes mid-sprint.
    Assess the potential impact on sprint goals, quality, and delivery timelines.
    Develop strategies to mitigate these risks and maintain sprint stability.

    Documentation and Tracking: Ensure that all changes made during the sprint are well-documented.
    Update sprint boards, task lists, and any related documentation to reflect the changes made and keep everyone aligned.

    Continuous Improvement: Use retrospectives at the end of the sprint to reflect on how the introduction of new changes impacted the team's performance and sprint outcomes.
    Learn from the experience to improve future sprint planning and handling of changes.

7) difference between Query and Path Parameter
8) API Status Code
9) Difference between Bug and Defect

"""


"""prints the number of occurrences of each character in a string.
Examples:

Input: str = "GeeksForGeeks"
Output:
r 1
s 2
e 4
F 1
G 2
k 2
o 1"""

input_str = "GeeksForGeeks"
freq = {}
for i in input_str:
    if i in freq:
        freq[i] = freq[i] +1
    else:
        freq[i] = 1

print(freq)




# ======================================================================================================================
# """ step 1) click on google URL
#     step 2) Search your Name
#     step 3) Click on "Search on google" Button
#     step 4) Find the number of results
#     step 5) check if result is greater than 50,000
#     step 6) if not,take screenshot of that page
#     step 7) print the number of results and 'your test case is failed'  """
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# service_obj = Service("C:\\Users\\Kunal\\PycharmProjects\\Selenium_project\\Drivers\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# # to enter name in text Box
# time.sleep(2)
# driver.find_element(By.NAME,"q").send_keys("kunal Sontakke")
#
# # click on "Google Search" Button
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,"gNO89b").click()
#
# # check if results number is greater than 50,000
# Result_Stats = driver.find_element(By.ID,"result-stats").text
#
# if "50,000" in Result_Stats:
#     assert True
# else:
#     driver.get_screenshot_as_file("Encora.png")
#     print(Result_Stats)
#     print("Your Test Case is Failed")

# =====================================================================================================================

"""python program to find palindrome"""
#
#
# input = str(input("Enter the String : "))
#
# reverse = input[::-1]
#
# if input == reverse:
#     print("the string is Palindrome")
# else:
#     print("the string is not palindrome")

