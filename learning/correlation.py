import math
from typing import List
from collections import Counter



def compatiblity(arr1 : List[float], arr2 : List[float]):
    if len(arr1) != len(arr2) or len(arr1) < 2:
        raise ValueError("Arrays must have the same length and at least 2 elements.")

    if any(not isinstance(i, (int, float)) for i in arr1 + arr2):
        raise ValueError("Both arrays must contain only integers or floats.")

    return True

# karl 's Correlation
def correlation(arr1, arr2):
    compatiblity(arr1,arr2)

    N = len(arr1)
    mean1 = sum(arr1) / N
    mean2 = sum(arr2) / N

    dev1, dev2 = [x - mean1 for x in arr1], [y - mean2 for y in arr2]
    numerator = sum([x * y for x,y in zip(dev1, dev2)])

    denominator = math.sqrt((sum(x**2 for x in dev1)) * (sum(y**2 for y in dev2)))

    return numerator / denominator if denominator != 0 else float('nan')


def rankify(array : List[float]):
    # duplicate and sort
    dummy = sorted(array)

    counter = Counter(dummy)
    ranks_dict = dict()

    r_no = 1
    i = 0
    while i < len(array):
        val = dummy[i]
        freq = counter[val]

        avg_rank = sum(range(r_no, r_no+freq)) / freq
        ranks_dict[val] = avg_rank

        r_no += freq
        i += freq

    return [ranks_dict[i] for i in array]


def spearman_correlation(arr1 : List[float], arr2 : List[float]):
    if compatiblity(arr1, arr2):
        ranks_X = rankify(arr1)
        ranks_Y = rankify(arr2)

        # calculate D = r1 - r2
        D = [(x - y)**2 for x,y in zip(ranks_X, ranks_Y)]   # **2 make it squared
        N = len(arr1)
        answer = 1 - ((6 * sum(D)) / (N * (N**2 - 1)))

        return answer




arr1 = [10, 20, 30, 40, 50]
arr2 = [5, 15, 25, 35, 45]

# Your function
my_result = spearman_correlation(arr1, arr2)

print("My Spearman Correlation:", my_result)

