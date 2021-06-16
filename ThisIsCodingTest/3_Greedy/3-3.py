# 3-3 숫자 카드 게임
# 난이도 하 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2019 국가 교육기관 코딩 테스트
# 풀이 시간 : 23분 소요

n, m = map(int, input().split())
card = []
sort_card = []

for i in range(n) :
  card.append(list(map(int, input().split())))
  card[i].sort()
  sort_card.append(card[i])

sort_card.sort(reverse=True)
print(sort_card[0][0])

# 코드 리뷰
# 아직 기본적인 파이썬 문법을 완벽하게 익히지 못한다. 그리고 책에 풀이된 풀이 방법과 다른데 특히 'sort_card.sort(reverse=True)'이 부분에서 정렬이 리스트의 각 행 0번째에 있는 값으로 정렬하는 것인지 모르겠어서 찾아보니 맨 첫번째 값부터 차례대로 정렬한다. sort보단 min, max함수를 이용하는 편이 좋은 답안이라고 생각한다.

# 리스트의 정렬에 관한 자료
# 1. [Python] 리스트/배열 정렬 함수 ( sort() / sorted() )
# https://dailyheumsi.tistory.com/67
# 2. 파이썬 정렬, 다중 조건으로 한 번에 하기.
# https://dev-note-97.tistory.com/13



# 3-3.py min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n) :
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력



# 3-3.py 2중 반복문 구조를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n) :
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data :
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력
