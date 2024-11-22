def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)

def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while (low < high) :
        while low <= right and A[low] <= pivot:
            low += 1

        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original  : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
