# http and Https
# api mocking
# =============================================================================================
def get_user_age(user):
    return user["age"]

def show_dictionary(user):
    return user["age"] if "age" in user else None

def print_dictionary(user):
    return user.get("age",None)


# ===================================================================
# Input: [1, 2, 3, 4, 5, 6]
# Output: [(1,6), (2,5), (3,4)]
inp1 =[1, 2, 3, 4, 5, 6, 7 ]
print([(i,j) for i in inp1 for j in inp1 if i+j==7 and i<j])
#  =====================================================================
envs = ['qa', 'stage', 'prod']
regions = ['us', 'eu']
versions = ['v1', 'v2']
# url = f"https://{envirnoment}.{region}.example.com/api/{verions}"

# expected output:
# https://qa.us.example.com/api/v1
# https://qa.us.example.com/api/v2
# https://qa.eu.example.com/api/v1
# https://qa.eu.example.com/api/v2
# https://stage.us.example.com/api/v1
# https://stage.us.example.com/api/v2
# https://stage.eu.example.com/api/v1
# https://stage.eu.example.com/api/v2
# https://prod.us.example.com/api/v1
# https://prod.us.example.com/api/v2
# https://prod.eu.example.com/api/v1
# https://prod.eu.example.com/api/v2
urls = []
for env in envs:
    for region in regions:
        for version in versions:
            urls.append(f"https://{env}.{region}.example.com/api/{version}")
            for url in urls:
                print(url)
# ===================================================================
list1 = [25, 36, 43, 34, 68, 53, 72]
#
# output = [72, 36, 43, 34, 68, 53, 25]
print(list1)
for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        list1[i], list1[j] =list1[j], list1[i]
print(list1)

