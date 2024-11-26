def sequential_search(A, key, low, high): #순차 탐색
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return -1

def sequential_search_transpose(A, key, low, high): #교환하기(한번 탐색된 값을 한 칸 앞으로 보내기) 전략이 추가된 순차 탐색
    for i in range(low, high+1):
        if A[i] == key:
            if low < i:
                A[i], A[i-1] = A[i-1], A[i]
                i = i -1
            return i
    return -1

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            binary_search(A, key, low, middle-1)
        else:
            binary_search(A, key, middle+1, high)
    return -1

def binary_search_iter(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1
