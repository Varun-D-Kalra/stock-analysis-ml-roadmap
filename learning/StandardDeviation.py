# code for Standard deviation calculation for a list of numbers or decimal values
import math


def standard_deviation(arr):
    if arr:
        if any(not isinstance(i, (int, float)) for i in arr):
            raise ValueError("All elements must be integers or floats.")
        if len(arr) < 2:
            raise ValueError("At least two values are required to compute standard deviation.")
        # if array is having data
        mean_x = sum(arr) / len(arr)
        variance = sum((x - mean_x) ** 2 for x in arr) / len(arr)
        return math.sqrt(variance)

        # code to accept values to calc SD
    data = []
    while True:
        try:
            value = input("Enter the values 1 by 1. Type quit to end the input data")
            if value.lower().strip() == "quit":
                break

            try:

                data.append(float(value))  # Convert input to float

            except ValueError:

                print("Invalid input! Enter a number, not a string or character.")

                continue  # Let user retry instead of exiting function

        except Exception as e:
            print(f"{e} happened")
            return

        # now data has values in it.
        # compute X**2 then perform variance calc
    if len(data) < 2:
        raise ValueError("At least two values are required to compute standard deviation.")

    mean_x = sum(data) / len(data)

    # Compute Variance
    variance = sum((x - mean_x) ** 2 for x in data) / len(data)

    return math.sqrt(variance)  # Return Standard Deviation
