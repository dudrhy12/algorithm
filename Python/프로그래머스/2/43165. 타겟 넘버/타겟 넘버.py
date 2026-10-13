def solution(numbers, target):
    answer = 0
    answer = dfs(answer, 0, numbers, target, 0)
    return answer

def dfs(answer, index, numbers, target, num):
    if index == len(numbers) and num == target:
        answer += 1
        return answer
    elif index == len(numbers):
        return answer
    else:
        plus_answer = dfs(answer, index+1, numbers, target, num+numbers[index])
        minus_answer = dfs(answer, index+1, numbers, target, num-numbers[index])
        return plus_answer + minus_answer
