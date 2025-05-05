#   This file is dedicated to build linear regression purely with numpy.

class Regression:

    def __init__(self, x, y):
        self.arr1 = x
        self.arr2 = y

    def mean(self, arr):
        return sum(arr) / len(arr)

    def bxy(self):
        xy = self.arr1 * self.arr2
        y_sq = self.arr2 * self.arr2

        return ((len(self.arr1) * sum(xy)) - (sum(self.arr1) * sum(self.arr2))) / ((len(self.arr1) * sum(y_sq)) - sum(self.arr1)**2)

    def eqn(self):