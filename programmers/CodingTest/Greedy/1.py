# 체육복 | 레벨 1 | 풀이 시간 : 40분 소요
'''
def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            # 여벌 체육복 가져온 학생이 체육복을 도난당한 경우 or 여벌 체육복을 다른 학생에게 빌려주는 경우
            if lost[i] == reserve[j] or lost[i] == reserve[j] + 1 or lost[i] == reserve[j] - 1 :
                reserve.pop(j)
                answer += 1
                break
    
    return answer
'''
# 코드 리뷰
# 정확성 테스트 테스트 12에서 실패가 뜨는데 이유를 모르겠다.
# 여벌 체육복 가져온 학생이 체육복을 도난당한 경우를 제일 우선적으로 처리해주어야 한다는 것을 고려하지 않았다.
# remove() -> 리스트의 인덱스가 아닌, 값을 받아서 지우는 방식
# pop(), del -> 리스트의 인덱스를 받아서 지우는 방식



# 1.py 답안 예시 (https://rain-bow.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5)
# set 자료형은 중복을 허용하지 않는 집합 자료형으로 객체끼리 집합연산 지원하기에 '-'기호를 이용해 각 집합별로 차집합 수행이 가능하다.
def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve :
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
    
    return n - len(set_lost)