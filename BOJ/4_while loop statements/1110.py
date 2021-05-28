#더하기 사이클

n = int(input())
m = n
t = int(0)

while True:
  if n < 10 :
    n += n
    t += 1
  else :
    if (n//10 + n%10) > 10 :
      n = n%10*10 + ((n//10 + n%10)%10)
      t += 1
    elif (n//10 + n%10) == 10 :
      n = n%10*10
      t += 1
    else :
      n = n%10*10 + (n//10 + n%10)
      t += 1

  if n == m :
    break

print(t)