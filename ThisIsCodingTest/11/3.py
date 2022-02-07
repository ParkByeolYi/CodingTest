# 3 문자열 뒤집기
# 난이도 하 | 풀이 시간 20분 | 시간 제한 2초 | 메모리 제한 128MB | 기출 핵심 유형
# 풀이 시간 : 분 소요
'''
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
'''

# 코드 리뷰
# 테스트 케이스를 추가해서 실행시켜도 정상 출력이 되는데 어디가 틀린지 모르겠다(확실한 것은 답안 예시가 더 깔끔하고 좋은 코드같다.)고 생각했으나 테케를 생각해서 더 추가해보니 첫 번째 원소에 대해서 처리하지 않아서 틀린 것이었다.
# input()에서 굳이 리스트에 넣지 않아도 원소에 접근할 수 있는 사실을 처음 알았고 전부 0이나 1로 바뀌는 경우로 접근해야 한다. 현재 수와 다음 수를 비교해서 같지 않은 경우에만 검사하는 방식으로 효율적으로 실행할 수 있다. 마지막으로 min함수를 이용하면 if-elif-else 구문을 사용하지 않아도 된다..!



# A03.py 답안 예시
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1' :
  count0 += 1
else :
  count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1) :
  if data[i] != data[i + 1] :
    # 다음 수에서 1로 바뀌는 경우
    if data[i + 1] == '1' :
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else :
      count1 += 1

print(min(count0, count1))
