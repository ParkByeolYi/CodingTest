# 2 곱하기 혹은 더하기
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 Facebook 인터뷰
# 풀이 시간 : 15분 소요

'''
s = input()
num = list(map(int, s))
result = num[0]

for i in range(1, len(num)) :
  if result == 0 :
    result += num[i]
  else :
    result *= num[i]

print(result)
'''

# 코드 리뷰
# '두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하면 된다.'
# if result <= 1 or num[i] <= 1 : 더하기 연산 else : 곱하기 연산 으로 처리하는 문제인데 테스트 케이스에서 나온 0에만 집중해서 풀어서 틀렸다. 나머지는 잘했다.

# 코드 수정
s = input()
num = list(map(int, s))
result = num[0]

for i in range(1, len(num)) :
  if result <= 1 or num[i] <= 1 :
    result += num[i]
  else :
    result *= num[i]

print(result)



# A02.py 답안 예시
'''
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)) :
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1 :
    result += num
  else :
    result *=num

print(result)
'''