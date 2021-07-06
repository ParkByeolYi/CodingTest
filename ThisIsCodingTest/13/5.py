# Q19 연산자 끼워 넣기
# 난이도 중 | 풀이 시간 30분 | 시간 제한 2초 | 메모리 제한 512MB | 기출 삼성전자 SW 역량테스트 | 링크 https://www.acmicpc.net/problem/14888
# 풀이 시간 : 16분 소요
'''
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_total = -1e9
max_result = 0
min_total = 1e9
min_result = 0

def b1(i):
  max_result = a[i] + a[i + 1]

def b2(i):
  max_result = a[i] - a[i + 1]

def b3(i):
  max_result = a[i] * a[i + 1]

def b4(i):
  max_result = a[i] // a[i + 1]

def bfs(count):
  for i in range(n):
    for j in range(len(b)):
      if j == 0:
        b1(i)
      elif j == 1:
        b2(i)
      elif j == 2:
        b3(i)
      elif j == 3:
        b4(i)

print(max(max_total, max_result))
print(min(min_total, min_result))
'''

# 코드 리뷰
# 최댓값, 최솟값 1e9 사용하는 것은 알았는데 뭐랑 비교해야할지 막막했다.



# A19.py 답안 예시
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, int(now / data[i]))
      div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
