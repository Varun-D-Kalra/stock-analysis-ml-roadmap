import numpy


class GreyScale:

    def __init__(self):
        pass

    def blur(self, matrix):
        rows, cols = matrix.shape
        kernel = numpy.array([1 / 9] * 9).reshape((3, 3))

        output = []

        for i in range(1, rows - 1):
            row = []
            for j in range(1, cols - 1):
                patch = matrix[i - 1:i + 2, j - 1:j + 2]
                blurred = numpy.sum(patch * kernel)
                row.append(blurred)
            output.append(row)

        return numpy.array(output)

image = [
    [52, 55, 61, 59, 79],
    [62, 59, 55, 104, 94],
    [63, 65, 66, 113, 144],
    [64, 70, 70, 126, 154],
    [69, 73, 74, 139, 154]
]

arr = numpy.array(image)
t = GreyScale()
print(t.blur(arr))


