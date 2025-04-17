# code for variance calculation for a list of numbers or decimal values
import math


def variance(arr):
    if any(not isinstance(i, (int, float)) for i in arr):
        raise ValueError("All elements must be integers or floats.")
    # if array is having data
    try:
        squares = [x**2 for x in arr]
        N = len(arr)
        return math.sqrt(((sum(squares)) / N) - ((sum(arr)) / N) ** 2)
    except IndexError:
        print("No operations can be done on empty data set ")


        # code to accept values to calc variance
        data = []
        while True:
            try:
                value = input("Enter the values 1 by 1. Type quit to end the input data")
                if value.lower().strip() == "quit":
                    break

                elif value.isalpha():
                    print("Invalid input. No characters allowed enter a number or decimal")

                else:
                    data.append(float(value))

            except Exception as e:
                print(f"{e} happened")
                return"RE run the program please"

        # now data has values in it.
        # compute X**2 then perform variance calc
        squares = [x**2 for x in data]
        N = len(squares)

        return math.sqrt(((sum(squares))/ N) - ((sum(data))/N)**2)
