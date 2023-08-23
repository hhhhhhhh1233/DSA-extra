import random

def maxSuffix(arr):
    if len(arr) <= 1:
        return arr[0], arr[0]

    maxSumLeft, totalSumLeft = maxSuffix(arr[:len(arr)//2])
    maxSumRight, totalSumRight = maxSuffix(arr[len(arr)//2:])

    if maxSumRight > (totalSumRight + maxSumLeft):
        return maxSumRight, totalSumLeft + totalSumRight
    else:
        return (totalSumRight + maxSumLeft), totalSumLeft + totalSumRight

def verifier(arr):
    sums = []
    for i, num in enumerate(arr):
        sums.append(arrSum(arr[i:]))
    greatest = sums[0]
    for i in sums:
        if i > greatest:
            greatest = i
    return greatest

def randArr(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(-20,20))
    return arr

def arrSum(arr):
    Sum = arr[0]
    for i in arr[1:]:
        Sum += i
    return Sum

testArr = randArr(10)
print(f"Testing with array: {testArr}")
print(f"maxSuffix() returns: {maxSuffix(testArr)[0]}")
print(f"verifier() returns: {verifier(testArr)}")
print(f"The total sum of the array is {maxSuffix(testArr)[1]}")
