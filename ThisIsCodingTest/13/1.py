# Q15 특정 거리의 도시 찾기
# 난이도 중하 | 풀이 시간 30분 | 시간 제한 2초 | 메모리 제한 256MB | 기출 핵심유형 | 링크 https://www.acmicpc.net/problem/18352
# 풀이 시간 : 분 소요
'''
n, m, k, x = map(int, input().split())
for i in range(m):
  cities = list(map(int, input().split))

def bfs(x, y):
  

for i in range(cities):
  for j in range(cities):
    result = bfs(i, j)
    if result == k:
      answer.append(print(result)
    else:
      print(-1)
'''



# A15.py 답안 예시
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1) :
  if distance[i] == k:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
  print(-1)



# 재풀이
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m) :
  a, b = list(map(int, input().split))
  graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
  now = q.popleft()
  for next_node in graph[now]:
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
