M = int(input())
N = int(input())
K = int(input())

arrays = [["B"]* N for i in range(M)]
count_g = 0

for i in range(K):
  choice = input().split()
  choice[1] = int(choice[1])

  if choice[0] == "R":
    for j in range(N):
      if arrays[choice[1] - 1][j] == "B":
        arrays[choice[1] - 1][j] = "G"
      else:
        arrays[choice[1] - 1][j] = "B"
  else:
    for elem in arrays:
      if elem[choice[1] - 1] == "B":
        elem[choice[1] - 1] = "G"
      else:
        elem[choice[1] - 1] = "B"

for row in arrays:
  for elem in row:
    if elem == "G":
      count_g += 1

print(count_g)