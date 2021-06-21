# 4-1 상하좌우
# 난이도 하 | 풀이 시간 15분 | 시간 제한 1초 | 메모리 제한 128MB
# 풀이 시간 : 12분 소요
'''
n = int(input())
data = list(input().split())
traveller = [1, 1]

for i in data :
  if i == 'L' and traveller[1]-1 != 0:
    traveller[1] -= 1
  elif i == 'R' and traveller[1] != n:
    traveller[1] += 1
  elif i == 'U' and traveller[0]-1 != 0:
    traveller[0] -= 1
  elif i == 'D' and traveller[0] != n:
    traveller[0] += 1

print(traveller)
'''



# 4-1.py 답안 예시
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]