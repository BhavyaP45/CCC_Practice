X = int(input())

x_viol = 0
x_constraints = []

for i in range(X):
    x_case = input().split()
    x_constraints.append(x_case)

Y = int(input())
y_constraints = []
y_viol = 0

for i in range(Y):
    y_case = input().split()
    y_constraints.append(y_case)

G = int(input())

for i in range(G):
    group = input().split()
    new_x = []
    for x in x_constraints:
      if (x[0] in group and x[1] not in group) or (x[1] in group and x[0] not in group):
          x_viol += 1
          x_constraints.remove(x)

    for y in y_constraints:
      if (y[0] in group and y[1] in group):
          y_viol += 1


print(y_viol + x_viol)

