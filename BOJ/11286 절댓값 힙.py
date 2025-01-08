class AbsoluteHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self.up_heap(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return 0

        if len(self.heap) == 1:
            return self.heap.pop()

        # 절댓값이 가장 작은 값을 반환
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # 마지막 요소를 루트로 이동
        self.down_heap(0)
        return min_value

    def up_heap(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.up_heap(parent)

    def down_heap(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.compare(self.heap[left], self.heap[smallest]):
            smallest = left

        if right < len(self.heap) and self.compare(self.heap[right], self.heap[smallest]):
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.down_heap(smallest)

    def compare(self, left, smallest):
        # 절댓값을 우선 비교, 같으면 실제 값 비교
        if abs(left) == abs(smallest):
            # 위 : -4, 왼쪽아래 : 4 라면 바꿀 필요가 없음 -> false
            return left < smallest
        return abs(left) < abs(smallest)


absolute_heap = AbsoluteHeap()
n = int(input())
input_list = []
for _ in range(n):
    input_list.append(int(input()))

for i in input_list:
    if i == 0:
        print(absolute_heap.pop())
    else:
        absolute_heap.push(i)
