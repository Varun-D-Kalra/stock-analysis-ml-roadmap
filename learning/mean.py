from typing import Optional,List
def mean(arr : Optional[List[float]] = None):

    if arr:

        if any(not isinstance(i, (int, float)) for i in arr):
            raise ValueError("All elements must be integers or floats.")
        return sum(arr) / len(arr)


        return total/len(arr)

    # if arr is empty ask for values
    values = []
    while True:
        user_input = input("Enter the value one by one. Type QUIT when done: ")

        if user_input.upper() == "QUIT":
            break

        try:
            values.append(float(user_input))
        except ValueError:
            print("Invalid input! Enter a number, not a string or character.")

    if values:
        total = sum(values)
        return total/len(values)
    if not values:
        raise ValueError("Cannot calculate mean of an empty list!")


