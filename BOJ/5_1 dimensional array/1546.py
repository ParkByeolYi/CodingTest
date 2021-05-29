#5	1546  평균
#평균을 조작하는 문제

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)
m = a[0]
total = int(0)

for i in a :
  total += i/m*100

print(total/n)