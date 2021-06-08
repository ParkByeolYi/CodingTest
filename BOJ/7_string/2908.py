#7	2908	상수
#숫자를 뒤집어서 비교하는 문제

num = list(map(int, input().split()))

num[0] = num[0]//100 + num[0]//10%10*10 + num[0]%100%10*100
num[1] = num[1]//100 + num[1]//10%10*10 + num[1]%100%10*100

if num[0] > num[1] :
  print(num[0])
else :
  print(num[1])