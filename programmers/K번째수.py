def solution(array, commands):
    answer = []
    for i in commands:
        copy_list = list(array)
        slice_list = copy_list[i[0]-1:i[1]]
        slice_list.sort()
        answer.append(slice_list[i[2]-1])
    return answer
