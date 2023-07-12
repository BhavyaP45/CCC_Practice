number = int(input())
num_sequence = 0
isGreater = False
if number > 720:
  divisor = number//(720)
  isGreater = True
  number = number % (720)

hour = 12
minute = 0

if isGreater:
  for i in range(720):
    minute += 1
    if minute == 60:
      minute = 0
      hour += 1

    if hour == 13:
      hour = 1

    if hour < 10:
      if minute % 10 - minute // 10 == minute//10 - hour % 10:
        num_sequence += 1


    else:
      if minute % 10 - minute // 10 == hour % 10 - hour//10 == minute//10 - hour % 10:
        num_sequence += 1

  num_sequence *= divisor
  hour = 12
  minute = 0

for i in range(number):
  minute += 1
  if minute == 60:
    minute = 0
    hour += 1
    if hour == 13:
      hour = 1

  if hour < 10:
    if minute % 10 - minute // 10 == minute//10 - hour % 10:
      num_sequence += 1


  else:
    if minute % 10 - minute // 10 == hour % 10 - hour//10 == minute//10 - hour % 10:
      num_sequence += 1


print(num_sequence)
