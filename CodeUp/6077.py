n = int(input())
s = 0
for i in range(1, n+1) : #range(시작, 끝)
  if i%2==0 :
    s += i

print(s)

'''
# while 반복실행구조를 이용한 코드
n = int(input())
s = 0
i = 1
while i<=n :
  if i%2==0 :
    s += i
  i = i+1

print(s)
'''