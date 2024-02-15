N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
sum = 0

for i in scores:
    sum = sum + i / max_score * 100

print(sum / N)

# test_n = input()
# test_scores = list(map(int, input().split()))
# max_score = max(test_scores)
# sum = sum(test_scores)

# new_avg = sum / max_score * 100 / int(test_n)

# print(new_avg)