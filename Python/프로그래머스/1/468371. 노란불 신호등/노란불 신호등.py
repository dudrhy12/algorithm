import math

def solution(signals):
    answer = -1
    
    periods = [sum(signal) for signal in signals]
    cycle = math.lcm(*periods)
    
    for i in range(1, cycle+1):
        all_yellow = True

        for signal in signals:
            if signal[0] <= (i-1) % sum(signal) < ( signal[0] + signal[1] ) :
                continue
            else:
                all_yellow = False

        if all_yellow:
            return i
    
    return answer