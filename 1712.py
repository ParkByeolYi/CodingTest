#1	1712	손익분기점
#이익이 발생하는 지점을 찾는 문제

n = list(map(int, input().split()))
i = 0
cost = n[0]+n[1]
income = n[2]*i

while True :
  try :
    income = n[2]*i
    
    if cost <= income :
      print(i)
      break

    i += 1
  except :
    print('-1')
