#4	3052  나머지
#위(3단계)와 비슷한 문제

a = []
b = []

for i in range(10) :
  a.append(int(input()))

for i in a :
  b.append(i%42)

b = list(set(b)) #리스트 중복 제거
print(len(b))