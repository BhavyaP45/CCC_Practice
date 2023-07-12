sequence = input()

array = [[1 , 2], [3 , 4]]
for char in sequence:
    if char == "H":
      array.reverse()
    else:
       for elem in array:
        elem.reverse()

for elem in array:
   print(*elem)