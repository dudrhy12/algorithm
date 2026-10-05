
def solution(n, w, num):
    answer = 0
    stacked_box = get_floor(n,w)
    num_direction = get_floor(num,w) % 2
    n_direction = get_floor(n,w) % 2
    if num_direction == n_direction and get_column(n,w) >= get_column(num,w):
        stacked_box += 1
    elif num_direction != n_direction and get_column(n,w) >= w - get_column(num,w):
        stacked_box += 1
    under_box = get_floor(num,w)
    answer = stacked_box - under_box
    return answer

def get_floor(box_number, w):
    if box_number % w == 0:
        return (box_number // w) - 1
    else:
        return box_number // w


def get_column(box_number, w):
    if box_number % w == 0:
        return w
    else:
        return box_number % w