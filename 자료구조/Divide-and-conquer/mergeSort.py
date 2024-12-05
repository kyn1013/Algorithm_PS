def merge(A, left, mid, right):
    k = left #병합을 위한 임시 리스트의 인덱스
    i = left #왼쪽 리스트의 인덱스
    j = mid+1 #오른쪽 리스트의 인덱스

    #값이 작은 부분 리스트의 요소를 sorted에 복사하고, 그 리스트의 인덱스를 증가, 어느 한쪽 부분이 모두 처리될 때까지 진행
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    #남은 부분 리스트의 모든 요소를 sorted로 복사
    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    #임시 리스트에 저장된 결과를 원래의 리스트A에 복사
    A[left:right+1] = sorted[left:right+1]


def merge_sort(A, left, right): #A[left..right]를 오름차순으로 정렬
    if left < right: #항목이 2개 이상인 경우
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)


