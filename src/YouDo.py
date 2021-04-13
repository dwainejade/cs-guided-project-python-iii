"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""


def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps  # O(log n)


"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""


def sorted_squares(A):
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
        if A[i] ** 2 < A[j] ** 2:
            ans.append(A[i] ** 2)
            i -= 1
        else:
            ans.append(A[j] ** 2)
            j += 1

    while i >= 0:
        ans.append(A[i] ** 2)
        i -= 1
    while j < N:
        ans.append(A[j] ** 2)
        j += 1

    return ans


"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


"""
Use a list comprehension to create a new list called new_list out of the numbers list. 
Use the list comprehension to make sure that the new_list only contains positive numbers and make sure they are cast as 
integers into the new_list.
"""

numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]
even_numbers = [number for number in numbers if number % 2 == 0]
new_list = [number for number in numbers if number > 0]
print(new_list)
