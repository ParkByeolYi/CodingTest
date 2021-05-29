#더하기 사이클

n = int(input())
m = n
t = int(0)

while True:
  a = n%10*10 #다음 십의 자리
  b = n//10 + n%10 #합계, 다음 일의 자리
  
  if n < 10 :
    n = a + b
    t += 1
  else :
    if b > 10 :
      n = a + b%10
      t += 1
    elif b%10 == 0 :
      n = a
      t += 1
    else :
      n = a + b
      t += 1

  if n == m :
    break

print(t)