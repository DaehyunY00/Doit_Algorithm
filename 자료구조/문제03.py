import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [0] * (n + 1) # 길이가 n+1 인 dp 배열을 0으로 초기화. 각 부분의 부분합을 저장.

for i in range(n):
    dp[i + 1] = dp[i] + numbers[i] # dp[i]는 numbers 배열의 첫 번째 원소부터 i-1번째 원소까지의 합을 저장
    
for i in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])