# 5 볼링공 고르기
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2019 SW 마에스트로 입학 테스트
# 풀이 시간 : 9분 소요
'''
n, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(n) :
  for j in range(n) :
    if data[i] != data[j] :
      result += 1

print(int(result/2))
'''
# 코드 리뷰
# 위 코드의 시간 복잡도는 O(N의 2제곱)이고 답안 예시의 시간 복잡도는 O(N)이므로 예시 코드가 더 좋은 코드이다.



# A05.py 답안 예시
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data :
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1) :
  n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n # B가 선택하는 경위의 수와 곱하기

print(result)
