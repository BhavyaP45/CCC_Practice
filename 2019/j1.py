Athree = int(input()) * 3
Atwo = int(input()) * 2
Aone = int(input())
Bthree = int(input()) * 3
Btwo = int(input()) *2
Bone = int(input())

Atotal = Athree + Aone + Atwo
Btotal = Bthree + Btwo + Bone
message = "T"

if Atotal < Btotal:
    message = "B"
elif Btotal < Atotal:
    message = "A"

print(message)