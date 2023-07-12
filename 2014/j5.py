num_students = int(input())
first_row = input().split()
second_row = input().split()
boole = "good"

for i in range(num_students):
    partners = [first_row[i], second_row[i]]

    second_partner_index = first_row.index(second_row[i])
    
    if second_row[second_partner_index] != partners[0] or  first_row[i] == second_row[i]:
        boole = "bad"
        break

print(boole)


