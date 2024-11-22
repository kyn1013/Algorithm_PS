def selection_sort(A):
    n = len(A)
    for i in range(0, n-1):
        least = i
        for j in range(i+1, n):
            if A[least] > A[j]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step %2d = "%(i+1), A)

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print("Step %2d = "%(i), A)

data = [6,3,7,4,9,1,5,2,8]
insertion_sort(data)
print(data)
