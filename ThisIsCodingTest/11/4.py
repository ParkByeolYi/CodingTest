# 4 만들 수 없는 금액
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 K 대회 기출
# 풀이 시간 : 12분 소요
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = list()

for i in range(n) :
  result.append(data[i])
'''

# 코드 리뷰
# 아예 모르겠다. 문제 해설을 보니 내가 그리디 알고리즘 유형을 정말 모른다는 것을 알겠다. 내가 생각했던 방식은 동전을 더해서 모든 경우의 수를 만들어 sort()해서 찾는 것인데 이 다음 해결방법이 없다.
# 답안 예시는 타겟을 설정해서 그 숫자에 적합하지 않으면 출력하는 방식이다.



# A04.py 답안 예시
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < x :
    break
  target += x

# 만들 수 없는 금액 출력
print(target)



# 답안 안 보고 작성
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
  if target < x :
    break
  target += x

print(target)
'''
