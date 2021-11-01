from FileReadWrite import *

DATA_FILE_PATH = 'multilineDATA.txt'

myFileHandle = openFileForWriting(DATA_FILE_PATH)



data1 = "here we go again \n writing lines of code and hoping they make sense"

writeALine(myFileHandle, data1)

myFileHandle2 = openFileForReading(DATA_FILE_PATH)

closeFile(myFileHandle)
closeFile(myFileHandle2)

myFileHandle = openFileForReading(DATA_FILE_PATH)
ReadALine(myFileHandle)
ReadALine(myFileHandle)