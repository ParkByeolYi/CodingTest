# 4-4 게임 개발
# 난이도 중 | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 128MB
# 풀이 시간 : 40분 소요
'''
n, m = map(int, input().split())
d = [0, 1, 2, 3] # 북 동 남 서
x, y, cd = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
result = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

map[x][y] = 2

# print(1, n, m, d, x, y, cd, map, result, dx, dy)
# print()

while '0' in str(map) :
  # print(2, n, m, d, x, y, cd, map, result, dx, dy)
  # print()
  if x + dx[cd] >= 0 and x + dx[cd] <= n and y + dy[cd] >= 0 and y + dy[cd] <= m and map[x + dx[cd]][y + dy[cd]] == 0 :
    map[x + dx[cd]][y + dy[cd]] = 2
    result += 1
    # print(3, n, m, d, x, y, cd, map, result, dx, dy)
    # print()

  for i in range(4) :
    if map[x + dx[i]][y + dy[i]] == 1 or map[x + dx[i]][y + dy[i]] == 2 :
      x -= dx[cd]
      y -= dx[cd]

  if map[x + dx[cd]][y + dy[cd]] == 1 or map[x + dx[cd]][y + dy[cd]] == 2 :
    if cd == 0 :
      cd = 2
    elif cd == 1 :
      cd = 3
    else :
      cd -= 2
  else :
    if cd == 0 :
      cd = 3
    else :
      cd -= 1

print(result)
'''
# 코드 리뷰
# 난이도 중인 이유를 알겠다. 생각해야 할 코드가 너무 많다. 2차원 리스트에 넣는 코드 정도는 머리에서 바로 나와야 한다.



# 4-4.py 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n) :
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def trun_left() :
  global direction
  direction -= 1
  if direction == -1 :
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
  # 왼쪽으로 회전
  trun_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else :
    turn_time += 1
  if turn_time == 4 :
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0 :
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else :
      break
    turn_time = 0

  # 정답 출력
  print(count)
