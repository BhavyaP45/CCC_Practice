
T = input()
S = input()

T_list = []
S_list = []

for char in T:
  T_list.append(char)

for char in S:
  S_list.append(char)


cyclicCheck = False
difference = len(T_list) - len(S_list)

for x in range(0, difference):
  if cyclicCheck:
    break

  S_list.clear()
  for char in S:
    S_list.append(char)

  if T_list[x] in S_list:
    for i in range(len(S_list) + 1):
      if len(S_list) == 0:
        isCyclic = "yes"
        cyclicCheck = True
        break
  
      if T_list[x + i] in S_list:
        index = S_list.index(T_list[x + i])
        a = S_list.pop(index)

else:
  isCyclic = "no"

print(isCyclic)
