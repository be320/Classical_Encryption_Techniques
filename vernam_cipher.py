import io
inputFile = open("./IO_Program Files/Vernam/vernam_plain.txt","r+")
inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)
results = []
cipher = ""

print("Enter Key for Vernam Cipher:")
key = input()
key.lower()

num_key = [ord(w) - 97 for w in key]

for msg in input_messages:
    msg = msg.lower()
    msg_length = len(msg)
    for i in range(len(msg)):
        letter = msg[i]
        cipher += chr(ord(letter) + num_key[i])
    print(cipher)
    results.append(cipher)
    cipher = ""

outputFile = open("./IO_Program Files/Vernam/vernam_plain_output_"+str(key)+".txt", "w", encoding="utf-8")
outputFile.write('\n'.join(results))
outputFile.close()
