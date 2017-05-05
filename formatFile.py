x = open("colourCodes.txt")
n = x.readlines()
x.close()
y = []
target = open("dictionaryNew.txt", 'w')
for line in n:
    y.append(line.strip().split('\t'))
z = []
for lst in y:
    for colour in lst:
        target.write(colour + ":\n")

target.close()
    

