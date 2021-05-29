#1  10818 최소, 최대
#최솟값과 최댓값을 찾는 문제

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0], a[len(a)-1])