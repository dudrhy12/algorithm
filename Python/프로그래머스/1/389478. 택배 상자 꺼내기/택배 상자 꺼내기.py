
def solution(n, w, num):
    answer = 0
    stacked_box = check(n,w)
    num_direction = check(num,w) % 2
    n_direction = check(n,w) % 2
    if num_direction == n_direction and check_2(n,w) >= check_2(num,w):
        stacked_box += 1
    elif num_direction != n_direction and check_2(n,w) >= w - check_2(num,w):
        stacked_box += 1
        print('here')
    print(stacked_box)
    under_box = check(num,w)
    print(under_box)
    answer = stacked_box - under_box
    return answer

def check(a,b):
    if a % b == 0 :
        return ( a // b ) -1
    else:
        return a // b
    
def check_2(a,b):
    if a % b == 0 :
        return b
    else:
        return a % b