# 3-2 큰 수의 법칙
# 난이도 하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2019 국가 교육기관 코딩 테스트
# 풀이 시간 : 24분 소요

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
total = 0

num.sort(reverse=True)

while m > 0 :
  if num[0] == num[1] :
    for _ in range(m) :
      total += num[0]
    m = 0

  elif m <= k :
    for _ in range(m) :
      total += num[0]
    m = 0

  else :
    for _ in range(k) :
      total += num[0]
    total += num[1]
    m -= k+1

print(total)

# 코드 리뷰
# 9 : 내림차순으로 정렬 -> 제일 큰 값과 두번째 큰 값을 변수로 저장하여 사용했으면 가독성이 높을 것 같다.
# 11~15 :? m을 0으로 만들기보단 break를 사용하면 더 빨리 끝내서 효율적인가 궁금하다.



# # 3-2.py 답안 예시
# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# data.sort() # 입력받은 수 정렬
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰 수

# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * K
# count += m % (k + 1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기

# print(result) #최종 답안 출력