from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
import numpy as np
import time

l = np.random.randint(0, 10, 1000)

# print(f"Array is:{l}")

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
    print(f"Megre sort execution: {(time.time() - start_time)}")

if __name__ == '__main__':
    print('---')
    bubbles()
    print('---')
    selection()
    print('---')
    insertion()
    print('---')
    merge()