results = []
cipher = ""
keys = []
print("Enter Key Dimension of Hill Cipher:")
dim = int(input())
print("Enter Key for Hill Cipher:")
if dim == 2:
    inputFile = open("./IO_Program Files/Hill/hill_plain_2x2.txt", "r+")
    print("(K1 K2)")
    print("(K3 K4)")
    for i in range(4):
        print("Enter K"+str(i+1)+":")
        keys.append(int(input()))
else:
    inputFile = open("./IO_Program Files/Hill/hill_plain_3x3.txt", "r+")
    print("(K1 K2 K3)")
    print("(K4 K5 K6)")
    print("(K7 K8 K9)")
    for i in range(9):
        print("Enter K" + str(i+1) + ":")
        keys.append(int(input()))

inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)

for msg in input_messages:
    msg = msg.lower()
    modified_msg = []
    ind = 0
    while ind < len(msg):
        modified_msg.append(msg[ind])
        if ind+1 == len(msg):
            modified_msg.append('x')
            break
        else:
            modified_msg.append(msg[ind+1])
            ind += 2

    while i < len(modified_msg):
        x1 = ord(modified_msg[i])
        x2 = ord(modified_msg[i+1])
        i += 2

