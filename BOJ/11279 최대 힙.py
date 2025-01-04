class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2 #오른쪽 자식의 경우는 -1을 해주고 2를 나눠줘야 부모가 올바르게 나오므로 1뺌
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def pop(self):
        if len(self.heap) == 0:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop() #힙에 1개만 있으면 바로 반환

        #1개 이상의요소가 있다면 최상단을 반환 후 가장 마지막에 있는 노드를 루트로 올리고 교환
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0) #자식 노드와 비교
        return max_value

    def _heapify_down(self, index):
        leftc = index * 2 + 1 #0인덱스로 넘겨서 1씩 더해줌
        rightc = index * 2 + 2
        largest = index

        #자식이 없는 경우에는 인덱스 초과하므로 앞의 길이 조건 추가
        if leftc < len(self.heap) and self.heap[leftc] > self.heap[largest]:
            largest = leftc
        if rightc < len(self.heap) and self.heap[rightc] > self.heap[largest]:
            largest = rightc

        #루트 노드가 자식노드와 변경되었다면 교환
        if index != largest:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

heap = MaxHeap()
n = int(input())
input_list = []

for _ in range(n):
    input_list.append(int(input()))

for i in input_list:
    if i == 0:
        print(heap.pop())
    else:
        heap.push(i)

