#A+B - 7

t = int(input())

for i in range(1, t+1) :
  a, b = map(int, input().split())
  print('Case #%d:'%i, a+b) #출력문 안에 %s:문자열 %d:정수 %f:부동소수점 작성 및 출력문구 뒤에 %변수명 or %값을 작성