def partition(A, left, right) :
    low = left + 1				    # 왼쪽 부분 리스트의 인덱스 (증가방향)
    high = right					# 오른쪽 부분 리스트의 인덱스 (감소방향)
    pivot = A[left] 				# 피벗 설정
    while (low <= high) :			# low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] <= pivot : low += 1
        while high>= left  and A[high] > pivot : high-= 1

        if low < high :			    # 선택된 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]	# 마지막으로 high와 피벗 항목 교환
    return high					    # 피벗의 위치 반환

def quick_select(A, left, right, k):
    pos = partition(A, left, right) #A에서 피벗의 인덱스

    if (pos+1 == left+k):
        return A[pos]
    elif (pos+1 > left+k):
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))

org = [27, 4, 26, 23, 34, 13, 42, 22, 48]
n = len(org)
array = list(org)
print("입력 리스트 =", array)
print("[축소정복] 최솟값: ", quick_select(array, 0, n-1, 1))
print()

array = list(org)
print("[축소정복] 최댓값: ", quick_select(array, 0, n-1, n))
print()

array = list(org)
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2))
print()

array.sort()
print("정렬 리스트 =", array)

array = [6, 5, 7, 9, 18, 3, 8]
n = 7
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2))
print()
