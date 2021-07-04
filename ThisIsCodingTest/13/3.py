# Q17 경쟁적 전염
# 난이도 중 | 풀이 시간 50분 | 시간 제한 1초 | 메모리 제한 256MB | 기출 핵심 유형 | 링크 https://www.acmicpc.net/problem/18405
# 풀이 시간 : 38분 소요
'''
n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * n for i in range(n)]
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(number):
  for i in range(n):
    for j in range(n):
      for l in range(4):
        if data[i][j] == number: # 1, 2, 3
          # print(i, j, number, l)
          nx = i + dx[l]
          ny = j + dy[l]
          if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if data[nx][ny] == 0:
              # print(nx, ny)
              temp[nx][ny] = number


def dfs(count):
  while count != s:
    count += 1
    for number in range(1, k + 1):
      virus(number)
      for i in range(n):
        for j in range(n):
          if data[i][j] == 0:
            data[i][j] = temp[i][j]
          # print('--------------------')
          # print(data[i][j])
          # print('--------------------')

dfs(0)
print(data[x-1][y-1])
'''
# 코드 리뷰
# for문을 너무 남발했다.



# A17.py 답안 예시
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
      data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
  virus, s, x, y = q.popleft()
  # 정확시 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
