def readContents(file):
    content = []
    with open(file) as f:
        for line in f:
            content.append(line.rstrip("\n"))
        return content

def createTags(fileName, numbers, points):
    for x in numbers:
        for y in points:
            processTags(fileName, x, y)

def processTags(fileName, x, y):
    f = open("build/" + fileName + ".txt", "a")
    tags = y.replace("01", x)
    f.write(tags + "\n")         

numbers = readContents('docs/numbers.txt')
exampleA = readContents('docs/points.txt')
createTags("exampleAouput", numbers, exampleA)