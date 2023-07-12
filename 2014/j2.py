num_of_votes = int(input())
votes = input()

count_a = 0
count_b = 0

for char in votes:
    if char == "A":
      count_a += 1
    else:
       count_b +=1

if count_a == count_b:
   print("Tie")
elif count_a < count_b:
   print("B")
else:
   print("A")