
def split(a):
    """Split array a into two halves with the larger half on the right for odd lengths."""
    middle = len(a)/2
    left = a[0:middle]
    right = a[middle:]
    return left, right

def merge(left, right):
    """Merge two sorted arrays into a concatenated sorted array."""
    leftindex = 0
    rightindex = 0
    m = []
    for k in range(len(left) + len(right)):
        if left[leftindex] < right[rightindex]:
            m.append(left[leftindex])
            leftindex += 1
            if leftindex == len(left): # We've completed the left side
                m.extend(right[rightindex:])
                break
        else:
            m.append(right[rightindex])
            rightindex += 1
            if rightindex == len(right): # We've completed the left side
                m.extend(left[leftindex:])
                break
    return m

def mergesort(a):
    """Use recursive merge sort (without any cleverness to reduce memory access)
    to sort the array a into a least first list.

    Returns sorted list.

    Assumes that all list elements are comparable"""

    # Deal with the base case
    if len(a) <= 1:
        return a

    # Recurse for everyone else
    left, right = split(a)
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
