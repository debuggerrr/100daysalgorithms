Given an array of integers, find the length of the longest subarray with a sum that equals to 0

a = [15, -2, 2, -8, 1, 7, 10, 23]


def findSubArrays(a):
    counter = 0
    d = {}
    sum = 0
    for i in range(len(a) - 1):
        sum = sum + a[i]
        if sum == 0:
            counter += 1  # This will check if the first position in the array is 0 itself then just return length by incrementing the counter by 1 i.e its max length
            return counter
        if sum in d.keys():
            counter = i - d[
                sum]  # This will subtract the index of the value from the array whose sum is already present in the dictionary. In our case it would be 5-0 (since sum was 15 at position 5 and it was already present in the 0th position)
        else:
            d[sum] = i  # If the sum is not present, then add it to the dictionary by assigning index as its value
    return counter


print(findSubArrays(a))
