import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = []

for i in range(n):
  data += [int(input())]

total, result = len(data)-1, 0

while k > 0:
  if data[total] > k:
    total -= 1
  elif data[total] <= k:
    num = int(k/data[total])
    k -= data[total] * num
    result += num

"""
while k > 0 and n != 1:
  if data[total] > k:
    total -= 1
  elif data[total] <= k:
    k -= data[total]
    result += 1

if n == 1:
  print(k)
  result = int(k/data[total])
"""

print(result)
