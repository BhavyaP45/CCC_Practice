n = int(input())
a_score = 100
d_score = 100

for i in range(n):
  round_scores = input().split()
  round_scores = [int(i) for i in round_scores]
  if round_scores[0] > round_scores[1]:
    d_score -= max(round_scores)
  elif round_scores[1] > round_scores[0]:
    a_score -= max(round_scores)

print(a_score)
print(d_score)
