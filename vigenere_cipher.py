inputFile = open("./IO_Program Files/Vigenere/vigenere_plain.txt","r+")
inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)
results = []
cipher = ""

print("Enter Key for Vigenere Cipher:")
key = input()
key.lower()

print("choose the mode you want :")
print("false: Repeating Mode  or true: Auto Mode")
mode = input()
mode.lower()


key_length = len(key)

for msg in input_messages:
    msg = msg.lower()
    msg_length = len(msg)
    num_key = [ord(w) - 97 for w in key]
    for ind in range(key_length,msg_length):
        if mode == "true":
            num_key.append(ord(msg[ind - key_length]) - 97)
        else:
            num_key.append(ord(key[ind % key_length])-97)
    for i in range(len(msg)):
        letter = msg[i]
        cipher += chr((ord(letter) + num_key[i] - 97) % 26 + 97)
    results.append(cipher)
    cipher = ""
    num_key = []

outputFile = open("./IO_Program Files/Vigenere/vigenere_plain_output_"+str(key)+"_"+str(mode)+".txt","w")
outputFile.write('\n'.join(results))
outputFile.close()
