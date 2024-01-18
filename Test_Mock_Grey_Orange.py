def sqr_decorator(func):
    def wrapper(*args):
        x = func(*args)

        return x ** 2
    return wrapper


def function(a):
    return a


function = sqr_decorator(function)
print(function(10))

# """'AAABBCCCDDDAACCCCEEF' >> 'A3B2C3D3A2C4E2F1'"""
#
# s = 'AAABBCCCDDDAACCCCEEF'
# # def func(s):
#     output = []
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             count += 1
#         else:
#             output.append(s[i-1])
#             output.append(str(count))
#             count = 1
#
#     output.append(s[-1])
#     output.append(str(count))
# #
#     return ''.join(output)
# #
# #
# # print(func(s))


s= 'AAABBCCCDDDAACCCCEEF'
def function(s):
    out = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            out.append(s[i-1])
            out.append(str(count))
            count = 1

    out.append(s[-1])
    out.append(str(count))

    return "".join(out)

print(function(s))
