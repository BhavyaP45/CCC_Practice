shelf_order = input()
list_shelf = [] 

for char in shelf_order:
  list_shelf.append(char)
num_swaps = 0

for i in range(len(shelf_order)):
  first_S = shelf_order.find("S")
  last_L = shelf_order.rfind("L")

  if first_S < last_L:
    list_shelf[first_S] = "L"
    list_shelf[last_L] = "S"
    num_swaps += 1

  elif last_L < first_S:
    break
  print(list_shelf)

  shelf_order = "".join(list_shelf)

if "M" in list_shelf:
    for i in range(len(shelf_order)):
        first_S = shelf_order.find("S")
        last_L = shelf_order.rfind("L")
        first_m = shelf_order.find("M")
        last_m = shelf_order.rfind("M")

        if first_m < last_L:
          list_shelf[first_m] = "L"
          list_shelf[last_L] = "M"
          num_swaps += 1

        elif first_m > first_S:
          list_shelf[first_m] = "S"
          list_shelf[first_S] = "M"
          num_swaps += 1

        elif last_m < last_L:
          list_shelf[last_m] = "L"
          list_shelf[last_L] = "M"
          num_swaps += 1

        elif last_m > first_S:
          list_shelf[last_m] = "S"
          list_shelf[first_S] = "M"
          num_swaps += 1
        shelf_order = "".join(list_shelf)


print(num_swaps)
