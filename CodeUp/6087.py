n = int(input())

for i in range(1, n+1) :
  if i%3==0 : #3의 배수일 경우 통과
    continue #다음 반복 단계로 넘어감
  print(i, end=' ') #i가 3의 배수가 아닐 때만 실행됨