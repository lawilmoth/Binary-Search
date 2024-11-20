import pytest
import random
from assignment import find_index_for_loop, find_middle_index, find_direction, binary_search
import time

def time_function(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    return elapsed_time

def test_find_index_for_loop():
    assert find_index_for_loop([1, 2, 3, 4, 5], 3) == 2
    assert find_index_for_loop([1, 2, 3, 4, 5], 6) == -1
    assert find_index_for_loop([10, 20, 30, 40, 50], 40) == 3
    assert find_index_for_loop([10, 20, 30, 40, 50], 25) == -1
    assert find_index_for_loop([], 1) == -1

def test_find_middle_index():
    assert find_middle_index([1, 2, 3, 4, 5]) == (2, 3)
    assert find_middle_index([1, 2, 3, 4]) == (1, 2)
    assert find_middle_index([10, 20, 30, 40, 50, 60]) == (2, 30)
    assert find_middle_index([10, 20, 30, 40, 50]) == (2, 30)
    assert find_middle_index([1]) == (0, 1)

def test_find_direction():
    assert find_direction([1, 2, 3, 4, 5], 3) == 0
    assert find_direction([1, 2, 3, 4, 5], 5) == 1
    assert find_direction([1, 2, 3, 4, 5], 1) == -1
    assert find_direction([10, 20, 30, 40, 50], 25) == -1
    assert find_direction([10, 20, 30, 40, 50], 5) == -1

def test_binary_search():
    
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([10, 20, 30, 40, 50], 40) == 3
    assert binary_search([10, 20, 30, 40, 50], 25) == -1
    
    random.seed(515)
    sum = 0
    lst = []
    for i in range(100):
        x = random.randint(1,10)
        sum += x
        lst.append(sum)

    assert binary_search(lst, 91) == 18

    lst = [i for i in range(100_000)]
    bin_time = time_function(binary_search, lst, 70_000)
    for_time = time_function(find_index_for_loop, lst, 70_000)

    assert bin_time < for_time