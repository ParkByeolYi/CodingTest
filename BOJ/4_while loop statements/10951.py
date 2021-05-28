#A+B - 4
#질문 검색 및 구글링 : 언제까지 입력받는지 정해두지 않아 try except 구문을 사용해야 함

while True :
  try :
    A, B = map(int, input().split())
    print(A+B)  
  except :
    break