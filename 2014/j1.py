angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

if angle_1 + angle_2 + angle_3 == 180:
    if (angle_1 != angle_2) and (angle_2 != angle_3) and (angle_1 != angle_3):
      print("Scalene")
    elif (angle_1 == 60) and (angle_2 == 60) and (angle_3 == 60):
       print("Equilateral")
    else:
       print("Isosceles")
else:
  print("Error")
