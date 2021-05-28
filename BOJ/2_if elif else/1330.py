#두 수 비교하기

a, b = map(int, input().split()) #공백으로 나누어 두 개의 값을 입력받아 map을 사용하여 변수 a, b에 int형으로 바꾸어 저장하도록 한다.

if a > b :
  print('>')
elif a < b :
  print('<')
elif a == b :
  print('==')