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


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


@timeit
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


table_size = 100000
# samples:
RandomArray = create_table(table_size, 1, table_size)

SortedArray = RandomArray[:]
SortedArray.sort()

ReversedArray = SortedArray[::-1][:]

print("For random data : ", end='')
heap_sort(RandomArray)
print("-----------------")
print("For sorted data : ", end='')
heap_sort(SortedArray)
print("-----------------")
print("For sorted in reverse order data : ", end='')
heap_sort(ReversedArray)
