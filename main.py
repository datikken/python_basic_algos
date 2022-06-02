from algos.bubble_sort import bubble_sort


def bubbles():
    l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
    print(f"Bubble sort array is:{l}")
    bubble_sort(l)
    print(f"Bubble sorted array is:{l}")


if __name__ == '__main__':
    bubbles()