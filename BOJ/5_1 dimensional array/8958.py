#6  8958  OX퀴즈
#OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제

n = int(input()) #테스트 케이스의 개수
case = [] #테스트 케이스를 담을 list

for i in range(n) :
  case.append(input())

for i in case :
  o = int(0) #연속하여 정답일 경우 1씩 증가
  count = int(0) #문자열의 몇 번째인지
  total = int(0) #총 합계

  for j in range(len(i)) :
    if i[count] == 'O' : #연속하여 문제를 맞힐 경우
      o += 1 #더할 값을 1씩 증가
      total += o
    elif i[count] == 'X' :
      o = 0
    count += 1
  
  print(total)