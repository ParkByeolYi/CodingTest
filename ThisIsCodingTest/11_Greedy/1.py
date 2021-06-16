# 1 모험가 길드
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 핵심 유형
# 풀이 시간 : 24분 소요

# inport time
# start_time = time.time() # 측정 시작

# 프로그램 소스코드
# end_time = time.time() # 측정 종료
# print("time :", end_time - start_time) # 수행 시간 출력

'''
n = int(input())
people = list(map(int, input().split()))
people.sort(reverse = True)
group = 0

for _ in range(n) :
  if len(people) < people[0] :
    break

  group += 1
  del people[0 : people[0]]
  
  if len(people) == 0 :
    break

print(group)
'''

# 코드 리뷰
# 처음에는 오름차순으로 하다가 중간에 내림차순으로 바꿔 코드를 작성했다. 왜 내림차순으로 바꿨을까? 분명 문제에서 모든 모험가를 특정한 그룹에 넣을 필요가 없다고 나왔고 머리로는 아는데 문제 풀기에 급해서 잘못 푼 것 같다. 그래서 다시 풀어본다. 위에 푼 문제는 공포도가 가장 큰 사람부터 그룹에 넣어야 한다고 생각한 문제라고 하면 될 것 같다.



# 풀이 시간 : 15분 소요
'''
n = int(input())
people = list(map(int, input().split()))
people.sort()
group = 0

for _ in range(n) :

  if (len(people) < people[0]) or len(people) == 0:
    break

  group += 1
  del people [0 : people[0]]
  
  if len(people) == 0 :
    break

print(group)
'''

# 코드 리뷰
# 2랑 3만 남았을 경우 어떻게 해결해야할지 모르겠다. A01.py 답안을 보니 '현재 그룹에 포함된 모험가의 수'를 변수로 생성하는 방법으로 문제를 해결했는데 공포도 확인도 하고 좋은 코드인 것 같다.



# A01.py 답안 예시
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1 # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    reult += 1 # 총 그룹의 수 증가시키기
    count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
