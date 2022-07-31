Find the first and last occurence of an given sorted array

a = [2, 5, 5, 5, 6, 6, 7, 7, 8]


def findMinMaxOccurence(a, k):
    res = []
    for i in range(len(a) - 1):
        if k == a[i]:
            res.append(i)
    return min(res), max(res)


print(findMinMaxOccurence(a, 5))
