def solution(sizes):
    answer = 0
    width = 0
    height = 0
    for i in range(len(sizes)):
        if (sizes[i][0] < sizes[i][1]):
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    for i in range(len(sizes)):
        if (width < sizes[i][0]):
            width = sizes[i][0]
        if (height < sizes[i][1]):
            height = sizes[i][1]
    answer = height * width
    return answer