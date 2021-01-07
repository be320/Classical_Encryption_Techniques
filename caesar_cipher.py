inputFile = open("./IO_Program Files/Caesar/caesar_plain.txt","r+")
inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)
results = []
cipher = ""

print("Enter Key for Caesar Cipher:")
key = int(input())

for msg in input_messages:
    msg = msg.lower()
    for i in range(len(msg)):
        letter = msg[i]
        cipher += chr((ord(letter) + key - 97) % 26 + 97)
    results.append(cipher)
    cipher = ""

outputFile = open("./IO_Program Files/Caesar/caesar_plain_output_"+str(key)+".txt","w")
outputFile.write('\n'.join(results))
outputFile.close()
