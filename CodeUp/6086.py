n = int(input())
s = c = 0 #여러개의 변수 선언하기

while True :
  s += c
  c += 1
  if s>=n :
    break #반복실행을 중단하고 가장 가까운 반복 블록의 밖으로 빠져나감

print(s)