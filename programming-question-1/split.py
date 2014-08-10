
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

def merge_and_count_split_inv(left, right):
    leftindex = 0
    rightindex = 0
    m = []
    z = 0
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
            z += len(left) - leftindex
            if rightindex == len(right): # We've completed the left side
                m.extend(left[leftindex:])
                break
    return m, z

def sort_and_count(a):
    """Count the number of split inversions in a and return a sorted version of a."""
    if len(a) <= 1:
        return a, 0
    left,right = split(a)
    l, x = sort_and_count(left)
    r, y = sort_and_count(right)
    sorteda, z = merge_and_count_split_inv(l,r)
    return (sorteda, x+y+z)

def main():
    """Calculate splits."""
    # Load in the array.
    array = [int(l) for l in open('IntegerArray.txt', 'r').readlines()]
    # Measure the number of split inversions compared to the ordered array.
    print sort_and_count(array)[1]
