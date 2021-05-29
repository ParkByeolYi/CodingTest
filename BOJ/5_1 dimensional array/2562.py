#2	2562  최댓값
#최댓값이 어디에 있는지 찾는 문제

a = []
b = int(0)

for i in range(9) :
  a.append(int(input()))

for j in a :
  if j > b :
    b = j

print(b)
print(a.index(b)+1) #리스트의 항목번호 출력