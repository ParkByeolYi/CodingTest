#2	4673	셀프 넘버
#함수 d를 정의하여 문제를 해결해 봅시다.

def d(n) :
  n = n + n//10 + n%10
  return n

a = list()
b = list()

for i in range(1, 10001) :
  a.append(d(i))
  b.append(i)

'''for i in range(1, 10001) :
  print(a[i])'''

for i in b :
  if i not in a :
    print(i)