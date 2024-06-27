def solution(str_list, ex):
    answer = ''
    a = []
    for i in str_list:
        if ex not in i:
            a += i
    answer = "".join(a)
        
    return answer