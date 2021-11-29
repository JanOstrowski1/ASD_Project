import random
import time
import functools
import sys

sys.setrecursionlimit(1000000)


def timeit(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsed_time * 1_000)))
        return result

    return new_func


def create_table(size, min, max):
    tab = []
    for i in range(0, size + 1):
        random_int = random.randint(min, max)
        tab.append(random_int)
    return tab


def partition(A, p, r):
    pivot = A[r]

    i = p - 1
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


@timeit
def quick_sort_timed(A, p, r):
    return quicksort(A, p, r)


table_size = 100000
# samples:
RandomArray = create_table(table_size, 1, 50)

SortedArray = RandomArray[:]
SortedArray.sort()

ReversedArray = SortedArray[::-1][:]

print("For random data : ", end='')
quick_sort_timed(RandomArray, 0, len(RandomArray) - 1)
print("-----------------")
print("For sorted data : ", end='')
quick_sort_timed(SortedArray, 0, len(SortedArray) - 1)
print("-----------------")
print("For sorted in reverse order data : ", end='')
quick_sort_timed(ReversedArray, 0, len(ReversedArray) - 1)
