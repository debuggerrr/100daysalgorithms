Find the maximum length of an subarray such that the sum is even

a = [2, 3, 5, 2, 6, 7]


def findSubArrays(a):
    res = []
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]  # Summing up all the values
    if sum % 2 == 0:
        return len(a)  # if sum of all the elements is even then return the original length
    for i in range(len(a)):
        if i != len(a) - 1:  # Checking whether i has reached the last position of the array
            sum = sum - a[i]  # Calculating the sum by subtracting the i value from the sum and storing it
            if sum % 2 == 0:  # Checking whether the sum is even
                res.append(
                    len(a[i + 1:]))  # If the sum is even then append the length of the remaining elements in a list
        if i == len(a) - 1:  # Checking whether i has reached the last position of the array
            sum = sum - a[i]  # Calculating the sum by subtracting the i value from the sum and storing it
            if sum % 2 == 0:  # Checking whether the sum is even
                res.append(len(a[
                               :-1]))  # This check is for the last element of an array. If by removing the last element from the sum, the sum is even
                # then return the all the length of previous elements before the last element
    return max(res)  # Returning max from the appended list


print(findSubArrays(a))
