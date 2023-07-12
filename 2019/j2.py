L = int(input())
list_of_messages = []
for i in range(L):
    code = input().split()
    code[0] = int(code[0])
    list_of_messages.append(code[0]*code[1])

print(*list_of_messages, sep = "\n")