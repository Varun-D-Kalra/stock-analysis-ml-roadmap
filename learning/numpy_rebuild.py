import math


class Numpy:
    def __init__(self):
        pass

    def usability(self, arr):
        try:
            if isinstance(arr[0], list):  # 2D array
                for row in arr:
                    for val in row:
                        if not isinstance(val, (int, float)) or math.isnan(val):
                            return False
            else:  # 1D array
                for val in arr:
                    if not isinstance(val, (int, float)) or math.isnan(val):
                        return False
            return True
        except Exception:
            return False

    def mean(self, arr):
        if not self.usability(arr):
            raise ValueError("Invalid data in array")

        if not arr:
            return 0

        if isinstance(arr[0], list):  # 2D
            flat = [item for sublist in arr for item in sublist]
            return sum(flat) / len(flat)
        else:  # 1D
            return sum(arr) / len(arr)


    def std(self, arr: list):
        if not arr:
            return "Empty data, cannot calculate std"

        if len(arr) == 1:
            return 0

        if self.usability(arr) != True:
            raise ValueError

        if arr.count(arr[0]) == len(arr):
            return 0

        mean = self.mean(arr)
        squares = [(x - mean)**2 for x in arr]

        return math.sqrt(sum(squares) / (len(arr) - 1))   # it does not matter if all values are same. returns 0

    def dot(self, A, B):
        if not A or not B:
            raise ValueError("Cannot multiply with empty arrays")

        if not self.usability(A) or not self.usability(B):
            raise ValueError("Incompatible Data Types in the Array")

        if len(A[0]) != len(B):
            raise Exception("The arrays fail the compatibility test")

        result = []
        # proper way to multiply matrices
        for row in range(len(A)):
            sub_row = []
            for col in range(len(B[0])):
                columns = [B[x][col] for x in range(len(B))]
                sub_row.append(sum([ele * c_ele for ele, c_ele in zip(A[row], columns)]))
            result.append(sub_row)

        return result
    def dot_1D(self, A, B):
        if len(A) != len(B):
            raise ValueError("Unequal Lengths")

        if not self.usability(A) or not self.usability(B):
            raise ValueError("Wrong Data type in the Arrays")

        if not A or not B:
            return None

        result = 0
        for a, b in zip(A, B):
            result = result + (a * b)

        return result

    def variance(self, A):
        if not A:
            raise ValueError("Empty arrays, cannot compute anything.")

        if not self.usability(A):
            raise ValueError("Wrong Data type in the Arrays")

        # make sure array is 1D not 2D
        if isinstance(A[0], list):
            raise ValueError("Invalid 2D array. Only 1D arrays are allowed for variance.")

        if len(A) < 2:
            raise ValueError("At least two values are required to compute variance.")

        mean = self.mean(A)
        deviations = [(x-mean)**2 for x in A]

        return (sum(deviations)) / (len(A)-1)

    def median(self, A):
        if not A:
            raise ValueError("Empty array, cannot compute Median")

        if not self.usability(A):
            raise ValueError("The array consists of some invalid data")

        if isinstance(A[0], list):
            raise ValueError("2D array is invalid please give only 1D arrays")

        if len(A) < 2:
            return "insufficient data in the array."

        # sorting step
        def quick_sort(arr):
            if len(arr) == 1:
                return arr

            pivot = arr[0]
            low =  [x for x in arr if x< pivot]
            high = [x for x in arr if x > pivot]

            return quick_sort(low) + [pivot] + quick_sort(high)

        sorted_arr = quick_sort(A)
        n = len(sorted_arr)

        if n % 2 == 1:  # Odd number of elements
            return sorted_arr[n // 2]

        else:  # Even number of elements
            mid1, mid2 = n // 2, (n // 2) - 1
            return (sorted_arr[mid1] + sorted_arr[mid2]) / 2


    def argmax(self, arr):
        if not arr:     # check for void
            raise ValueError("The array cannot be empty")

        if not self.usability(arr):     # check for valid input
            raise ValueError("Cannot process invalid data.")

        if isinstance(arr[0], list):    # for 2d array
            index = [0, 0]
            cur = arr[0][0]

            for row in range(len(arr)):
                for col in range(len(arr[row])):
                    if arr[row][col] > cur:
                        index = [row, col]
                        cur = arr[row][col]

            return index    # result for 2D matrix

        if isinstance(arr[0], (int, float)):    # code for 1D array
            index = 0
            cur = arr[0]

            for i in range(len(arr)):
                if arr[i] > cur:
                    cur = arr[i]
                    index = i

            return index
    def transpose(self, arr):
        if not arr:
            raise ValueError("Cannot accept empty matrices")

        if not self.usability(arr):
            raise ValueError("There exists invalid data in the array.")

        if not isinstance(arr[0], list):    # make sure its 2D
            raise TypeError("Only 2D matrices can be transposed")

        match = arr[0]      # make sure all sub arrays are of same length
        for x in arr:
            if len(x) != len(match):
                raise ValueError("The sub arrays are of unequal lengths.")

        result = []
        for cols in range(len(arr[0])):
            sub = []
            for row in range(len(arr)):
                sub.append(arr[row][cols])
            result.append(sub)

        return result



A = [
    [1,2,3],
    [4,5,7]
]

B = [
    [2,4],
    [7,8],
    [3,9]
]
obj = Numpy()
print(obj.dot(A, B))

print(obj.transpose(A))