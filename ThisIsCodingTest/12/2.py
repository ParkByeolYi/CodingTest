# Q08 문자열 재정렬
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 Facebook 인터뷰
# 풀이 시간 : 16분 소요

s = list(input())
n = []
s.sort()

for i in range(len(s)) :
  if ord(s[i]) - ord('A') < 0 :
    n.append(int(s[i]))

print(''.join(s)[len(n):], sum(n), sep = '')

# 코드 리뷰
# 리스트 대괄호, 콤마 없이 출력하는 방법을 찾아서 해결했다. ''.join(s)[:] 절대 잊지말아야 한다.
# 4-3 왕실의 나이트에서 사용했던 ord()함수를 이용해서 풀었다.
# isalpha() 함수를 사용하면 알파벳인지 확인할 수 있다.



# A08.py 답안 예시
'''
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data :
  # 알파벳인 경우 결과 리스트에 삽입
  if x.isalpha() :
    result.append(x)
  # 숫자는 따로 더하기
  else :
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에서 삽입
if value != 0 :
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
'''
