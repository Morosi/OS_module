import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filepath, textToWrite):
    fileHandle = open(filepath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filepath):
    if not fileExists(filepath):
        print("The file, " + filepath + "does not exist - cannot read it.")

    fileHandle = open(filepath, 'r')
    data = fileHandle.read()
    print(data)
    fileHandle.close()
    return data

def openFileForWriting(filepath):
    fileHandle = open(filepath, 'w')
    return fileHandle

def writeALine(fileHandle, lineToWrite):
    lineToWrite = lineToWrite + '\n'
    fileHandle.write(lineToWrite)

def openFileForReading(filepath):
    if not fileExists(filepath):
        print("The file, " + filepath + "does not exist - cannot read it.")
        return ''

    fileHandle = open(filepath, 'r')
    return fileHandle

def ReadALine(fileHandle):
    theLine = fileHandle.readline()
    if theLine.endswith('\n'):
        theLine = theLine.rstrip('\n')
    print(theLine)
    return theLine


def closeFile(fileHandle):
    fileHandle.close()

