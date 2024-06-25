def solution(my_string):
    answer = ''
    
    #ord(): 문자를 숫자로 변환하려는 경우, 아스키코드 사용할 때
    for i in range(len(my_string)):
        if (65 <= ord(my_string[i]) <= 90):
            answer += chr(ord(my_string[i]) + 32) #chr(): 숫자를 문자로 바꿈
        else:
            answer += chr(ord(my_string[i]) - 32)
    return answer