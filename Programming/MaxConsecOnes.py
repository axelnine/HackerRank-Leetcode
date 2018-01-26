input1 = [1,0,1,1,0,1,1,1,0]
possible = []
flag = 0
valid_inputs = [0,1]

for i in range(0,(len(input1))):
    if input1[i] not in valid_inputs:
        print("Invalid Input")
        break;
    if input1[i] == 1 and i == (len(input1)-1):
        flag = flag + 1
        possible.append(flag)
    elif input1[i] == 1:
        flag = flag + 1
    elif input1[i] == 0:
        possible.append(flag)
        flag = 0

print(max(possible))
