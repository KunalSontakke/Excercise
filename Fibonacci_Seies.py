# Print Fibonacci series.

# 1,2,3,5,8,13,21................

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return 0

    elif n == 1:
        return b

    else:
        for i in range(1, n + 1):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(6))

# =======================================================================================================================


def fibona(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    if n > 1:
        return fibona(n-1) + fibona(n-2)


print("file name is %s"%__name__)
if __name__ == "__main__":
    print(fibona(6))


def find_fibonacci_series(n):
    fibonacci_series = []
    if n < 0:
        return fibonacci_series
    if n == 0:
        fibonacci_series.append(0)
    else:
        fibonacci_series = [0,1]
        for i in range(2,n):
            next_term = fibonacci_series[i-1] + fibonacci_series[i-2]
            fibonacci_series.append(next_term)
    return fibonacci_series

print(find_fibonacci_series(9))
