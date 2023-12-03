
# Q.1 Find subarray with given sum without using any extra space A[] = {1,2,3,4,5} Output - 2,4
def subArraySum(arr, sum):
    """

    :param arr: represents an array with numbers
    :param sum: target sum
    :return: range of indices which equals to sum
    """
    for i in range(0, len(arr)):
        currentSum = arr[i]
        if currentSum == sum:
            print("Sum found at indexes", i)
            return
        else:
            for j in range(i + 1, len(arr)):
                currentSum += arr[j]
                if currentSum == sum:
                    print(f"{i},{j}")
                    return
    print("No Subarray Found")


if __name__ == "__main__":
    A = [1,2,3,4,5]
    sum = 15
    subArraySum(A, sum)


