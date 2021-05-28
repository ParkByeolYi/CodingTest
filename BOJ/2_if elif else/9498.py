#시험 성적

n = int(input()) #정수값 입력받음

if n <= 100 and n >= 90 :
  print('A')
elif n >= 80 :
  print('B')
elif n >= 70 :
  print('C')
elif n >= 60 :
  print('D')
else :
  print('F')