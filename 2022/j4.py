X = int(input())
violations = 0
x_constraints = []

for i in range(X):
    x_case = input().split()
    x_constraints.append(x_case)

Y = int(input())
y_constraints = []

for i in range(Y):
    y_case = input().split()
    y_constraints.append(y_case)

G = int(input())

for i in range(G):
    group = input().split()
    new_x = []
    for x in x_constraints:
      if (x[0] in group and x[1] not in group) or (x[1] in group and x[0] not in group):
          violations += 1
      else:
          new_x.append(x)
    x_constraints = new_x

    for y in y_constraints:
      if (y[0] in group and y[1] in group):
          violations += 1


print(violations)

