N = int(input())
total_array = []
for i in range(N):
    sequence = input()
    count_char = 1
    code_array = []
    for j in range(1, len(sequence)):
      char = sequence[j]
      charprev = sequence[j-1]

      if charprev == char:
        count_char += 1
      elif charprev != char:
        seq = str(count_char) + " " + charprev
        code_array.append(seq)
        count_char = 1
      
      if j == (len(sequence) - 1):
         seq = str(count_char) + " " + char
         code_array.append(seq)
 
    total_array.append(code_array)
      
for elem in total_array:
   print(*elem, sep = " ")