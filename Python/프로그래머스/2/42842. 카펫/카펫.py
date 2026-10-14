def solution(brown, yellow):
    answer = []
    total_num = brown + yellow
    for i in range(3, total_num // 3 + 1):
        if total_num % i == 0 and i >= total_num // i :
            width = i
            height = total_num // i
            if yellow == (width-2) * (height-2):
                answer.append(width)
                answer.append(height)
                break
    return answer