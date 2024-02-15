# 나머지 합 구하기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

remainder_count = [0] * M # M으로 나누었을 때 나머지가 i인 누적 합의 개수
cumulative_sum = 0 # 누적합
count = 0 # 구간 개수 세기

for num in A:
    cumulative_sum += num
    remainder = cumulative_sum % M # M으로 나눈 나머지
    if remainder == 0: # 나머지가 0이면 시작부터 현재까지의 합으로 M으로 나누어 떨어짐
        count += 1
    count += remainder_count[remainder] # 같은 나머지를 가진 누적 합의 개수만큼 더함
    remainder_count[remainder] += 1 # 나머지가 remainder인 누적 합의 개수 증가

print(count)
 
# # 나머지 합 구하기

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# A = list(map(input().split()))
# S = [0] * n
# C = [0] * m

# S[0] = A[0]
# answer = 0

# for i in range(1, n):
#     S[i] = S[i-1] + A[i]
    
# for i in range(n):
#     remainder = S[i] % m
#     if remainder == 0:
#         answer += 1
#     C[remainder] += 1

# for i in range(m):
#     if C[i] > 1:
#         answer += (C[i] * (C[i] - 1) // 2)


# print(answer)