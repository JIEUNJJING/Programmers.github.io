def solution(cipher, code):
    answer = ''
    
    #code - 1 해준 이유: 문자열 인덱스가 0부터 시작하기 때문
    for i in range (code - 1, len(cipher), code):
        answer += cipher[i]
    return answer