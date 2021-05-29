#7  4344  평균은 넘겠지
#과연 그럴까요?

c = int(input())
n = []

for i in range(c) :
  n.append(list(map(int, input().split()))) #list 속에 list 추가

for i in n :
  total = int(0) #모든 점수의 합계
  count = int(0) #평균 이상인 학생의 명수

  for j in range(1, i[0]+1) : #i[0]는 학생의 수이기 때문에 1부터 시작, N명까지
    total += i[j]

  for j in range(1, i[0]+1) :
    if total/i[0] < i[j] : #학생의 점수가 평균 이상일 경우
      count += 1

  count = count/i[0]*100 #평균을 넘는 학생들의 비율

  print('%.3f'%count + '%')