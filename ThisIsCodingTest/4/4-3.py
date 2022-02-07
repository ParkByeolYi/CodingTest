# 4-3 왕실의 나이트
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB
# 풀이 시간 : 16분 소요
'''
alphabet, number = list(input())
number = int(number) - 1
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(horizontal)) :
  if alphabet == horizontal[i] :
    alphabet = str(i)
    alphabet = int(alphabet)

result = 0
# print(alphabet, number)

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

for i in range(8) :
  alphabet += dx[i]
  number += dy[i]

  if alphabet < 0 or alphabet > 7 or number < 0 or number > 7 :
    # print(alphabet, number, i)
    alphabet -= dx[i]
    number -= dy[i]
    continue
  
  result += 1

  alphabet -= dx[i]
  number -= dy[i]

print(result)
'''
# 코드 리뷰
# 4-1.py의 상하좌우 문제와 비슷하다고 느껴서 dx, dy 리스트에 넣어서 코드를 작성해봤으며 조건문으로 8 x 8 좌표 평면을 벗어나지 않도록 했다.
# 아쉬운 점은 알파벳을 인트형으로 바로 바꾸지 않았고 알파벳, 숫자를 더했다 뺐다한 반복 부분이다.
# 답안 예시를 보니 column 변수 대입한 부분이 인상적이다. ord()함수를 이용해 숫자를 뺐다.
# 리스트 안에 튜플을 넣은 steps 변수를 이용해 반복문을 사용했다.(튜플은 한 번 선언된 값을 변경할 수 없다.)



# 4-3.py 답안 예시
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
    result += 1

print(result)
