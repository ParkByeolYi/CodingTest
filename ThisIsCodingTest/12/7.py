# Q13 치킨 배달
# 난이도 중 | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 512MB | 기출 삼성전자 SW 역량테스트 | 링크 https://www.acmicpc.net/problem/15686
# 풀이 시간 : 분 소요

# A13.py 답안 예시
from itertools import combinations

n, m = map(int, input().split())
chichen, house = [], []

for r in range(n) :
  data = list(map(int, input().split()))
  for c in range(n) :
    if data[c] == 1 :
      house.append((r, c)) # 일반 집
    elif data[c] == 2 :
      chichen.append((r, c)) # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chichen, m))

def get_sum(candidate) :
  result = 0
  # 모든 집에 대하여
  for hx, hy in house :
    # 가장 가까운 치킨집을 찾기
    temp = 1e9
    for cx, cy in candidate :
      temp = min(temp, abs(hx - cx) + abs(hy - cy))
    # 가장 가까운 치킨집까지의 거리를 더하기
    result += temp
  # 치킨 거리의 합 반화
  return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates :
  result = min(result, get_sum(candidate))

print(result)

# 코드 리뷰
# 구현은 익숙하지 않아서 머리가 백지장이 된다. 풀이 방법이 안 떠오를 때 해설을 보면서 작성한다.
# combinations은 조합 라이브러리로 모든 경우를 간단히 계산할 수 있다.
# 1e9 = 1*109 = 1000000000, 2e9 = 2*109 = 2000000000으로 2e9는 int 범위내에서 무한대 값
# abs()함수는 절댓값으로 만든다.
