import numpy as np
results = []
cipher = ""
keys = []
print("Enter Key Dimension of Hill Cipher:")
dim = int(input())
print("Enter Key for Hill Cipher:")
inputFile = open("./IO_Program Files/Hill/hill_plain_"+str(dim)+"x"+str(dim)+".txt", "r+")

if dim == 2:
    print("(K1 K2)")
    print("(K3 K4)")

else:
    print("(K1 K2 K3)")
    print("(K4 K5 K6)")
    print("(K7 K8 K9)")

for i in range(dim):
    row = []
    for j in range(dim):
        print("Enter K"+str(j+(i*dim)+1)+":")
        row.append(int(input()))
    keys.append(row)

inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)
subMsg = []


for msg in input_messages:
    msg = msg.lower()
    modified_msg = []
    ind = 0
    edits = len(msg) % dim
    modified_msg = [char for char in msg]
    if edits == 2:
        modified_msg.append('x')
    elif edits == 1:
        modified_msg.extend(['x', 'x'])
    i = 0
    while i < len(modified_msg):
        subMsg = []
        for ind in range(dim):
            subMsg.append(ord(modified_msg[ind+i])-97)
        subCipher = (np.dot(subMsg, keys) % 26) + 97
        for ind in range(dim):
            cipher += chr(subCipher[ind])
        i += dim
    results.append(cipher)
    cipher = ""

print(results)

outputFile = open("./IO_Program Files/Hill/hill_plain_"+str(dim)+"x"+str(dim)+"_output.txt","w")
outputFile.write('\n'.join(results))
outputFile.close()