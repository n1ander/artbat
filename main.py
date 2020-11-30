#takes file as argument and stores in an array
def readContents(file):
    content = []
    with open(file) as f:
        for line in f:
            #strip newlines and appends to content array
            content.append(line.rstrip("\n"))
        return content

#takes filename followed by two files as arguments
def createTags(fileName, numbers, points):
    for x in numbers:
        for y in points:
            processTags(fileName, x, y)

#writes tags to new file
def processTags(fileName, x, y):
    f = open("build/" + fileName + ".txt", "a")
    tags = y.replace("01", x)
    f.write(tags + "\n")         

numbers = readContents('docs/numbers.txt')
exampleA = readContents('docs/points.txt')
createTags("exampleAouput", numbers, exampleA)