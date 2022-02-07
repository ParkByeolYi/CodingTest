# Q09 문자열 압축
# 난이도 중하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2020 카카오 신입 공채 | 링크 https://programmers.co.kr/learn/courses/30/lessons/60057
# 풀이 시간 : 15분 소요
'''
def solution(s):
    result = []
    for i in range(len(s)) :
        result.append(s[i])
    return result
'''

# 코드 리뷰
# 입출력 예 #5를 이해하지 못해 해설을 보고 이해하고 답안을 외웠다.



# A09.py 답안 예시
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1) :
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step] :
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
