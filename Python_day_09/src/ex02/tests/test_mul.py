import pytest
from sys import path
import time
path.append('../')
import multiply_base
import multiply

def test_mul():
    matrix = [[i for i in range(100)] for _ in range(100)]

    start_time = time.time()
    res_base = multiply_base.mul(matrix, matrix)
    end_time = time.time()
    base_time = end_time - start_time
    
    start_time = time.time()
    res_cython = multiply.mul(matrix, matrix)
    end_time = time.time()
    cython_time = end_time - start_time
    assert res_base == res_cython and base_time > cython_time

test_mul()
