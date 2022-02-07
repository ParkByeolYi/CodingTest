# Q07 럭키 스트레이트
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 256MB | 기출 핵심 유형 | 링크 https://www.acmicpc.net/problem/18406
# 풀이 시간 : 5분 소요

n = list(map(int, input()))
first = n[:int(len(n)/2)]
second = n[int(len(n)/2):]

if sum(first) == sum(second) :
  print('LUCKY')
else :
  print('READY')

# 코드 리뷰
# 이제 백준 브론즈 문제를 잘 푸는 것 같아서 뿌듯했다.



# A07.py 답안 예시
'''
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2) :
  summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length) :
  summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summay == 0 :
  print("LUCKY")
else :
  print("READY")
'''
