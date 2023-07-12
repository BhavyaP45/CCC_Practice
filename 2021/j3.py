
number = 0
last_direction = ""
direction = ""
list_of_code = []
while number != 99999:
    number = int(input())
    ten_thousand = number//10000
    thousand = number//1000 % 10
    rest = number % 1000

    if number == 99999:
        continue
    
    if (ten_thousand + thousand) % 2 == 1:
        direction = "left"
        last_direction = direction
    elif (ten_thousand + thousand) != 0 and (ten_thousand + thousand) % 2 == 0:
        direction = "right"
        last_direction = direction
    else:
        direction = last_direction
    
    list_of_code.append(direction + " " + str(rest))

print(*list_of_code, sep = "\n")
  

    
