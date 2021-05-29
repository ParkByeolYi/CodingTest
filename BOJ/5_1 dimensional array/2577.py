#3	2577  숫자의 개수
#각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제

#더 깔끔한 코드
A = int(input())
B = int(input())
C = int(input())

D = str(A*B*C) #AxBxC 계산한 결과

for i in range(10) : #0부터 9까지
  print(D.count(str(i))) #다시 int로 바꾸어 줄 필요가 없음

'''
A = int(input())
B = int(input())
C = int(input())

D = A*B*C #AxBxC 계산한 결과
D = str(D)
N = int(0)

while N != 10 :
  N = str(N)
  print(D.count(N))
  N = int(N)
  N += 1
'''