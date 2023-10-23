from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free

cdef int **remake_matrix(list m):
    cdef int m_row = len(m)
    cdef int m_col = len(m[0])
    cdef int **A = <int**>PyMem_Malloc(m_row * sizeof(int *))
    for i in range(m_row):
        A[i] = <int*>PyMem_Malloc(m_col * sizeof(int))
    
    for i in range(m_row):
        for j in range(m_col):
            A[i][j] = m[i][j]
    return A

cdef free_matrix(int **m, rows):
    for i in range(rows):
        PyMem_Free(m[i])
    PyMem_Free(m)

cpdef list mul(list m1, list m2):
    cdef int m1_rows = len(m1)
    cdef int m1_cols = len(m1[0])
    cdef int m2_rows = len(m2)
    cdef int m2_cols = len(m2[0])
    cdef int **new_m1 = remake_matrix(m1)
    cdef int **new_m2 = remake_matrix(m2)

    cdef list result = [[0] * m2_cols for _ in range(m1_rows)]
    for i in range(m1_rows):
        for j in range(m2_cols):
            for k in range(m1_cols):
                result[i][j] += new_m1[i][k] * new_m2[k][j]

    free_matrix(new_m1, m1_rows)
    free_matrix(new_m2, m2_rows)
    return result