instructions = input()
instructions_list = []

list_letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "123456789"
index = 0
for i in range(1,len(instructions)):
   if instructions[i] in list_letters:
      if instructions[i-1] in numbers:
         instructions_list.append(instructions[index: i])
         index = i 
    
   if i == len(instructions) - 1:
      instructions_list.append(instructions[index: i + 1])

   
for i in range(len(instructions_list)):
    string_letter = ""
    command = ""
    turns = ""
    for elem in instructions_list[i]:
        if elem in list_letters:
          string_letter += elem
        elif elem == "-":
          command += "loosen"
        elif elem == "+":
           command += "tighten"
        else:
           turns += elem
    
    print(string_letter, command, turns)

