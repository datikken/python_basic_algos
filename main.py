from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
import numpy as np
import time

l = np.random.randint(0, 1000, 1000)

def bubbles():
    start_time = time.time()
    bubble_sort(l)
    # print(f"Bubble sorted array is: {l}")
    print(f"Bubble sort execution: {(time.time() - start_time)}")

def selection():
    start_time = time.time()
    selection_sort(l)
    # print(f"Selection sorted array is: {l}")
    print(f"Selection sort execution: {(time.time() - start_time)}")

def insertion():
    start_time = time.time()
    insertion_sort(l)
    # print(f"Insertion sorted array is: {l}")
    print(f"Insertion sort execution: {(time.time() - start_time)}")

def merge():
    start_time = time.time()
    merge_sort(l)
    print(f"Merge sort execution: {(time.time() - start_time)}")

def std_sorted():
    start_time = time.time()
    sorted(l)
    print(f"Std sorted execution: {(time.time() - start_time)}")

def quick():
    start_time = time.time()
    quick_sort(l)
    # print(l)
    print(f"Quick sorted execution: {(time.time() - start_time)}")


if __name__ == '__main__':
    print('---')
    bubbles()
    print('---')
    selection()
    print('---')
    insertion()
    print('---')
    merge()
    print('---')
    std_sorted()
    print('---')
    quick()