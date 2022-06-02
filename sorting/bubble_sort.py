# Bubble sort is a simple sorting algorithm used to rearrange a set of elements in ascending or descending order.
# It's useful for smaller sets of elements but is inefficient for larger sets.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]