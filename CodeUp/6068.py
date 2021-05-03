n = int(input())

if n>=90 :
  print('A')
else :
  if n >= 70 :
    print('B')
  else :
    if n >= 40 :
      print('C')
    else :
      print('D')

#elif는 else if 의 짧은 약어로 elif 사용시 if ... else ... 구조를 겹쳐 사용할 때처럼, 여러번 안 쪽으로 들여쓰기 하지 않아도 됨