    # code to find covariance between 2 variables

    def cov(arr1: list, arr2:list)->float:
        if len(arr1) != len(arr2) or len(arr1) < 2 or len(arr2)< 2:
            raise ValueError("The calculation is not possible due to wrong data")

        if not all(isinstance(x, (float, int)) for x in arr1 + arr2):
            raise ValueError("Both arrays must contain only float values.")

        n = len(arr1)

        mean_x = (sum(x for x in arr1)) / n
        mean_y = (sum(x for x in arr2)) / n

        deviation_x = [x - mean_x for x in arr1]
        deviation_y = [x - mean_y for x in arr2]

        prod = sum([x*y for x,y in zip(deviation_x, deviation_y)])

        covariance = prod / (n - 1)

        return covariance

    X = [1.0]
    Y = [2.0]

    print(cov(X, Y))