#2	4673	셀프 넘버
#함수 d를 정의하여 문제를 해결해 봅시다.

numbers = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10_000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)

'''
#100이하의 수에서는 잘 출력되나 9900번대에서 출력이 이상함
#참고할 비슷한 방법으로 풀이
#https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-4673%EB%B2%88-%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84

def d(n) :
  if n >= 100 :
    n = n + n//100 + n%100//10 + n%100%10
  elif n >= 1000 :
    n = n + n//1000 + n%1000//100 + n%1000%100//10 + n%1000%100%10
  else :
    n = n + n//10 + n%10

  return n

a = list()
b = list()

for i in range(1, 10001) :
  a.append(d(i))
  b.append(i)

for i in b :
  if i not in a :
    print(i)
'''