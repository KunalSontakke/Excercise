# lis1 = ['00:00', '11:59', '12:00', '01:59']
# min_diff = 0
# for i in range(len(lis1)-1):
#     if int(lis1[i]) - int(lis1[i+1]) > min_diff:
#         min_diff = int(lis1[i]) - int(lis1[i+1])
# print(min_diff)


def find_factorial(n):
    factorial = 1
    if n == 0:
        return 0
    if n ==1 :
        return 1
    else:
        for i in range(1,n+1):
            factorial = factorial * i
    return factorial
print(find_factorial(5))

"""5 * 4 * 3 * 2 * 1"""

def find_prime(n):
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is prime number")

find_prime(3)

# ===============================================================
json1 ={
    "query": {
        "bool": {
            "must": [{"match": {"message.x_request_id": "123450"}}],
            "filter": [
                {
                    "range": {
                        "@timestamp": {
                            "gte": "2025-11-11T11:34:33Z",
                            "lte": "2025-11-17T11:34:33Z",
                            "time_zone": "+05:30"
                        }
                    }
                }
            ]
        }
    }
}

print(json1["query"]["bool"]["filter"][0]["range"]["@timestamp"]['gte'])
count = 0
# for key,value in json1.items():
#     if isinstance(value,str):
#         count += 1
#
# print(count)
