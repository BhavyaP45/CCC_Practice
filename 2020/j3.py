N = int(input())
array_of_coordinates = [[] , []]

for i in range(N):
  coordinate = input().split(",")
  array_of_coordinates[0].append(int(coordinate[0]))
  array_of_coordinates[1].append(int(coordinate[1]))

array_of_coordinates[0].sort()
array_of_coordinates[1].sort()

bottom_left_frame_x = str(array_of_coordinates[0][0] - 1)
bottom_left_frame_y = str(array_of_coordinates[1][0] -1)

top_right_frame_x = str(array_of_coordinates[0][-1] + 1)
top_right_frame_y = str(array_of_coordinates[1][-1] + 1)

print(bottom_left_frame_x + "," + bottom_left_frame_y)
print(top_right_frame_x + "," + top_right_frame_y)