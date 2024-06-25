def solution(my_string):
    answer = 0
    
    for i in my_string:
        if i.isdigit(): #숫자인지 확인하는 함수 사용
            answer += int(i) #i는 문자열이기 때문에 형변환 해주기
            
    return answer