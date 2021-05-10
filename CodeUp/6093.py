n = int(input())
a = input().split()

for i in range(n-1, -1, -1) : #a에 저장된 값들을 거꾸로 출력하기 위해 range(시작, 끝, 증감)을 큰 수에서 작은 수로 가도록 작성
  print(a[i], end=' ')

'''
a = map(int, input().split())는 왜 안 되는 걸까? TypeError: 'map' object is not subscriptable 오류뜸
'''