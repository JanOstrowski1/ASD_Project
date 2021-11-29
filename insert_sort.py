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


@timeit
def insert_sort(A):
    for i in range(1, len(A)):
        x = A[i]

        j = i - 1

        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = x

    return A


table_size = 100000
# samples:
RandomArray = create_table(table_size, 1, table_size)

SortedArray = RandomArray[:]
SortedArray.sort()

ReversedArray = SortedArray[::-1][:]



print("For random data : ", end='')
insert_sort(RandomArray)
print("-----------------")
print("For sorted data : ", end='')
insert_sort(SortedArray)
print("-----------------")
print("For sorted in reverse order data : ", end='')
insert_sort(ReversedArray)
