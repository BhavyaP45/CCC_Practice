temp = int(input())

P = temp * 5 - 400
sealevel = 0

if P < 100:
    sealevel = 1
elif P > 100:
    sealevel = -1
  
print(P)
print(sealevel)