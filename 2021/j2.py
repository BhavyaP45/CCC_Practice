N = int(input())
winner = ""
highest_bid = 0

for i in range(N):
    person = input()
    amount = int(input())

    if amount > highest_bid:
      highest_bid = amount
      winner = person

print(winner)