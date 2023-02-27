import csv
folderPath = "D:/Food_Detection_Project/darknetTest/training/trainingCoffeAndPizza/images/"
fileName = "/bb_info.txt"
groundTruthPath ="D:/Food_Detection_Project/darknetTest/training/trainingCoffeAndPizza/images/1_backup/ground-truth-1/"
filePathForName="D:/Food_Detection_Project/darknetTest/training/trainingCoffeAndPizza/images\yolo.names"
counter = 1
arrayOfFiles = []
sortedArray = []
namesArray=[]


def createNewArrayWithNames(namesArray2, sortedArray4):
    newArray=[]
    if (len(sortedArray4)>1):
        for arry in range(len(sortedArray4)):
            sortedArray4[arry][0] = namesArray2[sortedArray4[arry][5]-1]
            newArray.append(sortedArray4[arry][0:5])
    else:
        sortedArray4[0][0] = namesArray2[sortedArray4[0][5]-1]
        newArray.append(sortedArray4[0][0:5])
    return newArray


def storeIntoFile(sortedArray2, counter2):
    with open(groundTruthPath + str(counter2) + ".txt", 'w', newline='') as csvFile3:
        writer = csv.writer(csvFile3, delimiter=' ')
        sortedArray3 = []
        sortedArray3 = createNewArrayWithNames(namesArray, sortedArray2)
        for rows in sortedArray3:
            writer.writerow(rows)

for i in range(1, 100):
    if i == 1:
        filePath = folderPath + str(i) + fileName
        with open(filePath, newline='') as csvFile:
            reader = csv.reader(csvFile, delimiter=" ")
            next(reader)
            fileArray = []
            for row in reader:
                tempArray = []
                tempArray = row
                tempArray.append(i)
                fileArray.append(list(map(int, tempArray)))
            arrayOfFiles = arrayOfFiles + fileArray
    else:
        break
sortedArrayofFile = sorted(arrayOfFiles,key=lambda x:x[0])
#print(sortedArrayofFile)

with open(filePathForName) as csvFile2:
    reader = csv.reader(csvFile2)
    for row in reader:
        print (row[0])
        namesArray.append(row[0])
    #print(namesArray)

for i in range(len(sortedArrayofFile)):
    if sortedArrayofFile[i][0] == counter:
        sortedArray.append(sortedArrayofFile[i])
    else:
        storeIntoFile(sortedArray, counter)
        counter = sortedArrayofFile[i][0]
        sortedArray.clear()
        sortedArray.append(sortedArrayofFile[i])