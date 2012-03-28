"""Programming Question 2 - Quicksort."""
import random
import numpy as np

def choose_pivot_random(A, l, r):
    return random.randint(l, r-1)

def choose_pivot_first(A, l, r):
    return l

def choose_pivot_final(A, l, r):
    return r-1

def choose_pivot_median3(A, l, r):
    indexes = np.array([l, (r-1), (l+r-1)/2])
    entries = np.array(A)[indexes]
    return indexes[entries.argsort()[1]]

def partition(A, l, r):
    """Partion A from l to r around the element A[l] and return the position of the partition element."""
    i = l+1
    p = A[l]
    for j in range(l+1, r):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l],A[i-1] = A[i-1], A[l]
    return i-1

def _qs(A, l, r, choose_pivot):
    """Sort A in region l to r."""
    n = r - l 
    if n <= 1: # Nothing to do in base case
        return 0
    p = choose_pivot(A, l,r)
    A[l], A[p] = A[p], A[l]
    pe = partition(A, l, r)
    # Pivot is now in the correct position
    # Partition the two parts of the array.
    #count += max((pe - l - 1),0) + max((r - (pe+1) - 1),0)
    ncomp = r - l - 1
    ncomp += _qs(A, l, pe, choose_pivot)
    ncomp += _qs(A, pe+1, r, choose_pivot)
    return ncomp

def qs(A, choose_pivot=choose_pivot_random):
    """Perform quicksort."""
    return _qs(A, 0, len(A), choose_pivot)

def test(choose_pivot):
    A = load_entries()
    count = qs(A, choose_pivot)
    print count

def load_entries():
    return [int(l) for l in open('QuickSort.txt', 'r').readlines()]
