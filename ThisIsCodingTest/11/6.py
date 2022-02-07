# 6 무지의 먹방 라이브
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2019 카카오 신입 공채
# 풀이 시간 : 30분 소요
'''
def solution(food_times, k):
    answer = 1
    
    for i in range(k) :
        if food_times[answer-1] != 0 :
            food_times[answer-1] -= 1
        answer += 1
            
        if answer > len(food_times)-1 :
            answer = 1
    
    return answer
'''

# 코드 리뷰
# food_times에 하나씩 접근해서 값을 줄이고 answer 값을 1씩 증가해서 풀어보려 했으나 마음대로 실행되지 않았다.



# A06.py 답안 예시
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k :
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)) :
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key =lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
