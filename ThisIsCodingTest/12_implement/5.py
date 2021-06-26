# Q11 뱀
# 난이도 중 | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 삼성전자 SW 역량테스트 | 링크 https://www.acmicpc.net/problem/3190
# 풀이 시간 : 30분 소요
'''
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k) :
  column, row = map(int, input().split())
  board[column - 1][row - 1] = 1

l = int(input())
for _ in range(k) :
  x, c = list(input().split())
  x = int(x)

i = 0
time = 0 # 몇 초
snake = [0, 0] # 뱀 위치

# print(111, n, k, l, x, c, time, board)

while True :
  print(222, n, k, column, row, l, x, c, time, board)

  # 뱀이 사과를 먹을 경우
  if snake in board :
    snake.append()

  # 게임 시작 시간으로부터 x초가 끝난 뒤
  if time == x :
    # 왼쪽으로 90도 방향을 회전
    if c[i] == 'L' :
      print('')
    # 오른쪽으로 90도 방향을 회전
    elif c[i] == 'D' :
      print('')
    i += 1

  time += 1
'''
# 코드 리뷰
# 뱀이 어떻게 자기자신의 몸과 부딪히는지 모르겠다.



# A11.py 답안 예시
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k) :
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l) :
  x, c = input().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c) :
  if c == 'L' :
    direction = (direction - 1) % 4
  else :
    direction = (direction + 1) % 4
  return direction

def simulate() :
  x, y = 1, 1 # 뱀의 머리 위치
  data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
  direction = 0 # 처음에는 동쪽을 보고 있음
  time = 0 # 시작한 뒤에 지난 '초' 시간
  index = 0 # 다음에 회전할 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True :
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2 :
      # 사과가 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0 :
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] == 1 :
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪혔다면
    else :
      time += 1
      break
    x, y = nx, ny # 다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0] : # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())