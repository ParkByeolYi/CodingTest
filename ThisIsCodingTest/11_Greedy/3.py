# 3 문자열 뒤집기
# 난이도 하 | 풀이 시간 20분 | 시간 제한 2초 | 메모리 제한 128MB | 기출 핵심 유형
# 풀이 시간 : 분 소요

s = input()
num = list(map(int, s))
next_zero = 0
next_one = 0

for i in range(1, len(num)) :
  if num[i-1] == 1 and num[i] == 0 :
    next_zero += 1
  elif num[i-1] == 0 and num[i] == 1 :
    next_one += 1

if next_zero > next_one :
  print(next_one)
else :
  print(next_zero)

# 코드 리뷰
