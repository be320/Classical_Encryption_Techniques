inputFile = open("./IO_Program Files/PlayFair/playfair_plain.txt","r+")
inputData = inputFile.read().splitlines()
inputFile.close()
num_of_messages = int(inputData[0])
input_messages = inputData
input_messages.pop(0)
results = []
cipher = ""
playfairArray=[]
playfairMatrix=[]
alphabet=[]
pairs =[]

print("Enter Key for PlayFair Cipher:")
key = input()
key = key.lower()

for i in range(26):
    alphabet.append(chr(97+i))

for letter in key:
    if letter in alphabet:
        playfairArray.append(letter)
        alphabet.remove(letter)

for letter in alphabet:
    playfairArray.append(letter)

playfairArray.remove('j')

for i in range(5):
    row=[]
    for j in range(5):
        row.append(playfairArray[j+(i*5)])
    playfairMatrix.append(row)

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


for msg in input_messages:
    msg = msg.lower()
    modified_msg = []
    ind = 0
    while ind < len(msg):
        modified_msg.append(msg[ind])
        if ind+1 == len(msg):
            modified_msg.append('x')
            break
        elif msg[ind] == msg[ind+1]:
            modified_msg.append('x')
            ind += 1
        else:
            modified_msg.append(msg[ind+1])
            ind += 2
    i = 0

    modified_msg = [w.replace('j', 'i') for w in modified_msg]
    print(modified_msg)
    while i < len(modified_msg):
        (x1, y1) = index_2d(playfairMatrix, modified_msg[i])
        (x2, y2) = index_2d(playfairMatrix, modified_msg[i+1])
        if (x1 != x2) and (y1 != y2):
            cipher += playfairMatrix[x1][y2]
            cipher += playfairMatrix[x2][y1]
        elif x1 == x2:
            cipher += playfairMatrix[x1][(y1+1) % 5]
            cipher += playfairMatrix[x2][(y2+1) % 5]
        else:
            cipher += playfairMatrix[(x1 + 1) % 5][y1]
            cipher += playfairMatrix[(x2 + 1) % 5][y2]

        i += 2
    results.append(cipher)
    cipher = ""

print(results)

outputFile = open("./IO_Program Files/Playfair/playfair_plain_output_"+key+".txt","w")
outputFile.write('\n'.join(results))
outputFile.close()


