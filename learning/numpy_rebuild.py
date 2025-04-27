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