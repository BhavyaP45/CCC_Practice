P = int(input())
N = int(input())
R = int(input())

day = 0
total_infected = N

while total_infected <= P: 
  N *= R
  total_infected += N
  day += 1

print(day)

