class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self.up_heap(len(self.heap) - 1) #추가한 값의 인덱스 전송

    def up_heap(self, index):
        parent = (index - 1) // 2
        if self.heap[parent] > self.heap[index] and index > 0:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.up_heap(parent)

    def pop(self):
        if len(self.heap) == 0:
            return 0

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.down_heap(0)
        return min_value

    def down_heap(self, index):
        left_c = (index * 2) + 1
        right_c = (index * 2) + 2
        minimum = index

        #자식들 중에서 가장 작은 애로 인덱스 교환
        if left_c < len(self.heap) and self.heap[left_c] < self.heap[minimum]:
            minimum = left_c

        if right_c < len(self.heap) and self.heap[right_c] < self.heap[minimum]:
            minimum = right_c

        if index != minimum:
            self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
            self.down_heap(minimum)

heap = MinHeap()
n = int(input())
input_list = []

for _ in range(n):
    input_list.append(int(input()))

for i in input_list:
    if i == 0:
        print(heap.pop())
    else:
        heap.push(i)
