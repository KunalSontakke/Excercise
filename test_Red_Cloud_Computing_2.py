# """Input: "aabcccccaaa"
# Output: "a2b1c5a3"
#
# Input: "abcdef"
# Output: "abcdef"""
#
# def compression_str(a):
#     out = ""
#     count = 1
#     flag = False
#     for i in range(1,len(a)):
#         if a[i] == a[i-1]:
#             count += 1
#             flag = True
#         else:
#             out += a[i-1] + str(count)
#             count =1
#     out += a[-1] + str(count)
#     if flag == False:
#         temp = ""
#         for i in out:
#             if i.isalpha():
#                 temp += i
#         out = temp
#     print(out)
#
#
#
# compression_str("abcdef")


# ======================================================================================================================

def test_bb():
    assert True

def test_aa():
    assert True



