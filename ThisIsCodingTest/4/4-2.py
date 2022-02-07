# 4-2 시각
# 난이도 하 | 풀이 시간 15분 | 시간 제한 2초 | 메모리 제한 128MB
# 풀이 시간 : 15분 소요
'''
n = int(input())
result = 0

hour = [3, 13, 23]
times = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

for i in range(n) :
  if i in hour :
    result += 1*60*60
    # print(1, i, hour, result)

  for j in range(60) :
    if j in times : 
      result += 1*60
      # print(2, j, times, result)
    if j in times :
      result += 1*60
      # print(3, j, times, result)

print(result)
'''

# 코드 리뷰
# 위 코드는 3이 시, 분, 초에 중복으로 나올 경우의 수를 고려하지 않고 세었기에 잘못된 코드이다.
# 'if i in hour'와 'if j in times'의 뜻을 이제 안다. (보통 string형으로 사용한다.)
# i가 hour 리스트에 있을 경우 true이면 j가 times에 있을 경우 true이면 아래의 코드를 실행한다.



# 4-2.py 답안 예시
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1) :
  for j in range(60) :
    for k in range(60) :
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k) :
        count += 1

print(count)
