# 3-4 1이 될 때까지
# 난이도 하 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2018 E 기업 알고리즘 대회
# 풀이 시간 : 8분 소요

'''
n, k = map(int, input().split())
result = 0

while True :
  if n%k == 0 :
    while n != 1 :
      n = int(n/k)
      result += 1
    break
  else :
    n -= 1
    result += 1

print(result)
'''
# 코드 리뷰
# 문제에 나온 예시 입력값으로 했을 때는 1씩 뺐을 때 k가 n의 제곱형태로 나누어지기 때문에 위의 코드가 가능했으나 제곱형태가 아닌 경우의 수를 생각하지 못했다.
# 3-4.py 답안 예시에서 target 설정해서 result 값을 증가시키는 코드는 for문을 사용하지 않고 쓸 수 있는 멋진 코드로 시간 단축을 확실하게 할 수 있으므로 반드시 기억했다 사용하겠다.



# 3-4.py 답안 예시
# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True :
  # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target
  
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k :
    break
  
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)



# # 3-4.py 답안 예시 : 코드 안 보고 작성
# n, k = map(int, input().split())
# result = 0

# while True :
#   target = (n // k) * k
#   result += (n - target)
#   n = target

#   if n < k :
#     break
  
#   result += 1
#   n //= k

# result += (n - 1)
# print(result)
