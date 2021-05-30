#1  15596 정수 N개의 합
#함수를 구현해 봅시다.

def solve(a) :
  ans = 0
  for i in range(len(a)) :
    ans += a[i]
  return ans