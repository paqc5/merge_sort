"""

Paola Quevedo
CS5001
Homework 5
February 29, 2020

Test Case 1
Input: [1, 6, 3, 8, 2, 9, 2, 0, 5]
Output: [0, 1, 2, 2, 3, 5, 6, 8, 9]

Test Case 2
Input: [100, 500, 1, 0, -2, 6]
Output: [-2, 0, 1, 6, 100, 500]

Test Case 3
Input: [1, 3, 10, 20, 50, 60, 90]
Output: [1, 3, 10, 20, 50, 60, 90]

Test Case 4
Input: [15, 12, 11, 10, 8, 6]
Output: [6, 8, 10, 11, 12, 15]

Test Case 5
Input: [6, 4, 1, 1, 2, 0]
Output: [0, 1, 1, 2, 4, 6]

"""


def merge_sort(numbers):
    """
        Param: list numbers: list to sort
        Return: list result: a sorted list
        Does: it divides the list until it gets one param and then compares the
        values and creates a new sorted list
    """
    # If there is just one value in the list return it
    if len(numbers) <= 1:
        return numbers

    # Find the half of the list
    middle = len(numbers) // 2
    left = []
    right = []

    # Storage one half of numbers in left and the other half in right
    for i in range(0, middle):
        left.append(numbers[i])

    for j in range(middle, len(numbers)):
        right.append(numbers[j])

    # Divide the lists again
    left = merge_sort(left)
    right = merge_sort(right)

    # Call the function merge
    result = merge(left, right)
    return result


def merge(left, right):
    result = []

    # Run the while until there are not elements in left or right
    while len(left) > 0 and len(right) > 0:

        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    # If there is any element left in left or right, add it to result
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    # Return the merged list
    return result
