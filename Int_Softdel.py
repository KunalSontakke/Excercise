""" [4:17 PM] ManuSingh Sikarwar
1.SDLC
2.Test cases/scenarios for LinkedIn
Sure, here are some test scenarios for LinkedIn, the professional networking platform:

    Login Functionality:
        Verify that users can log in using valid credentials (email/username and password).
        Verify the system prevents login with invalid credentials and displays appropriate error messages.
        Verify the "Remember me" functionality remembers the user's session after logging out and logging back in.

    Profile Management:
        Test the ability to edit/update profile information such as name, headline, summary, experience, education, skills, and contact information.
        Test profile picture upload and validation of supported image formats and size limits.
        Verify that changes made to the profile are reflected accurately and consistently across the platform.

    Networking and Connections:
        Test the functionality to send, accept, and reject connection requests.
        Validate the ability to search for connections using different criteria (name, company, location, etc.) and send connection requests.
        Verify that notification alerts are received and displayed for new connection requests.

    Messaging and Communication:
        Test the ability to send messages to connections and verify the delivery and receipt of messages.
        Validate the formatting options (e.g., bold, italic, hyperlink) and attachments in messages.
        Test the notification system for new messages and message read status.

    Job Search and Applications:
        Verify the functionality to search for job openings based on various criteria (keywords, location, industry, etc.).
        Test the application submission process for jobs, ensuring proper validation and submission confirmation.
        Validate the receipt of application status updates and notifications.

    Groups and Discussions:
        Test the creation, joining, and participation in groups and discussions.
        Verify that users receive notifications for group invitations, new discussions, or replies to their posts.

    Privacy and Security Settings:
        Validate the privacy settings for the profile, ensuring users can control who sees their information.
        Test two-factor authentication setup and account security options.
        Verify that changes made to privacy settings are applied correctly and reflected in the user's profile.

    Mobile Application Testing:
        Test LinkedIn's mobile app functionality, ensuring features work seamlessly on different mobile platforms (iOS, Android).
        Validate responsiveness, UI/UX, and performance on mobile devices.

3.Pytest framework
4.Openpyxl,Requests

"""

# """
# 1)Base POM
# - element lovators
# 2)
# REST API Cleint
# - REst API
# 3)Configuration
# -config
# -conftest
# 4)Utilities
# -
# 5) GUI Automation
# - Web pages
# 6) Test Scripts
# - test cases
# 7_ repost
# html
# 8) Logs
# - logs
# """
# import pytest
#
#
# @pytest.mark.parametrize("username,passowrd",[("kunal","kunal123"),("manu","manu123")])
#
# def test_login(username,passowrd):
#     assert "sontakke" in username
#


# ======================================================================================================================

"""
A

AB

ABC

ABCD

ABCDE
# """
#
# str = "ABCDE"
# for i in range(6):
#     for j in range(len(str)):
#         print(j,end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(chr(64 + j), end="")
#     print()
#
#
# lis = []
# dic = {"name":"kunal","lastname":"sontakke"}
# print(dic)
#
# dic["age"] = 29
#
# print(dic)
# # key =
# # dic
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()
