# code to format data like pandas using numpy
import numpy
class MiniTable:

    def __init__(self, arr):
        self.arr = arr

    def shape(self):
        return self.arr.shape
    def sum(self, axis):
        return self.arr.sum(axis = axis)

    