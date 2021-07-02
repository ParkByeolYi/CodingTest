# Q16 연구소
# 난이도 중 | 풀이 시간 40분 | 시간 제한 2초 | 메모리 제한 512MB | 기출 삼성전자 SW 역량테스트 | 링크 https://www.acmicpc.net/problem/14502
# 풀이 시간 : 60분 소요
'''
from itertools import permutations

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
zeros = []
result = 0

for i in range(n):
  for j in range(m):
    if data[i][j] == 0:
      zeros.append([i, j])

for zero in list(permutations(zeros, 3)):
  data[zero] = 1
  
  for i in range(n):
    for j in range(m):
      if data[i][j] == 2:
        if i > 0 or i < n or j > 0 or j < m:
          if i - 1 != 1 or i + 1 != 1 or j - 1 != 1 or j - 1 != 1:
            data[i][j] = 2

  for i in range(n):
    for j in range(m):
      if data[zero] == 0:
        result += 1

  data[zero] = 0

print(max(0, result))
'''



# A16.py 답안 예시
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
