import random
import time
import functools


def create_table(size, min, max):
    tab = []
    for i in range(0, size + 1):
        random_int = random.randint(min, max)
        tab.append(random_int)
    return tab


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


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


@timeit
def merg_sort_timed(A):
    merge_sort(A)


table_size = 100000
# samples:
RandomArray = create_table(table_size, 1, table_size)

SortedArray = RandomArray[:]
SortedArray.sort()

ReversedArray = SortedArray[::-1][:]



print("For random data : ", end='')
merg_sort_timed(RandomArray)
print("-----------------")
print("For sorted data : ", end='')
merg_sort_timed(SortedArray)
print("-----------------")
print("For sorted in reverse order data : ", end='')
merg_sort_timed(ReversedArray)
