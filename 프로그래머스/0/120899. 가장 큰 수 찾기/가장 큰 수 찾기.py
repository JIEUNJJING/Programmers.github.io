def solution(array):
    answer = []
    max_val = array[0]
    
    for i in range(1, len(array)):
        if(array[i] > max_val): # 최댓값 찾기
            max_val = array[i]
            max_idx = i
    answer = [max_val, max_idx]
    return answer