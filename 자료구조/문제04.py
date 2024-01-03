import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[0] * (n+1)] # 2차원 배열 값 저장. n+1 x n+1
D = [[0] * (n+1) for _ in range(n+1)] # 각 지점까지의 부분합을 저장할 2차원 dp 배열 모든 값이 0으로 초기화

# n개 행에 대한 데이터를 입력 받아 A 배열을 업데이트. 각 행의 시작에는 0이 추가되어 인덱스가 1부터 시작되도록함. 
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# D[i][j]: A배열의 (1,1) ~ (i, j)까지의 부분합.
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] +A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)


# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split()) # n: row, m: col

# array = []

# for _ in range(n):
#     array.append(list(map(int, input().split())))

# sum_dp = [[0] * (n+1) for _ in range(n + 1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         sum_dp[i][j] = sum_dp[i][j-1] + sum_dp[i-1][j] - sum[i-1][j-1] + array[i-1][j-1]
        
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     ans = sum_dp[x2][y2] - sum_dp[x2][y1-1] - sum_dp[x1-1][y2] + sum_dp[x1-1][y1-1]
#     print(ans)
    