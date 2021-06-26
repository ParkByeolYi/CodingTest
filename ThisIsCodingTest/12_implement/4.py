# Q10 좌물쇠와 열쇠
# 난이도 중하 | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2020 카카오 신입 공채 | 링크 https://programmers.co.kr/learn/courses/30/lessons/60059
# 풀이 시간 : 10분 소요

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a) :
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n) :
        for j in range(m) :
            result[j][n - i - 1] = a[i][j]
    return result

# 좌물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 좌물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 좌물쇠의 중앙 부분에 기존의 좌물쇠 넣기
    for i in range(n) :
        for j in range(n) :
            new_lock[i + n][j + n] = lock[i][j]
            
    # 4가지 방향에 대해서 확인
    for rotation in range(4) :
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2) :
            for y in range(n * 2) :
                # 좌물쇠에 열쇠를 끼워 넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 좌물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True :
                    return True
                # 좌물쇠에서 열쇠를 다시 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] -= key[i][j]
    return False

# 코드 리뷰
# 문제가 이해가 안 돼서 답안 해설을 보고 코드를 외웠다.
# 난이도가 중하인데 체감상 매우 어렵다. 더 많은 문제들을 다뤄봐야겠다.
# 이 문제에서는 특히 좌물쇠의 크기를 기존의 3배로 변환하여 문제를 푼 것이 신기했다.