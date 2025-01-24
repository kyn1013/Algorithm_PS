def solution(sizes):
    rotated = []
    # 가로, 세로 길이 중에서 더 긴 값을 가로로 두기 -> 돌린다
    for i in sizes:
        if i[0] < i[1]:
            i = [i[1], i[0]]
        rotated.append(i)

    # 모든 명함이 들어갈 수 있는 크기여야 하기 때문에 최댓값 추출
    max_w = max(i[0] for i in rotated)
    max_h = max(i[1] for i in rotated)

    return max_w * max_h
