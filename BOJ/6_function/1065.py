#3	1065	한수
#X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다.

n = int(input())
result = 0

for i in range(1, n + 1):
  if i <= 99: # 1부터 99까지는 모두 한수
    result += 1

  else:
    data = list(map(int, str(i))) # 숫자를 자릿수대로 분리
    if data[0] - data[1] == data[1] - data[2]: #등차수열 확인
      result += 1

print(result)

# 참고 블로그 : https://roseline124.github.io/algorithm/2019/03/29/Algorithem-baekjoon-1065.html
