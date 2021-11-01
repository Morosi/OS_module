import random

from FileReadWrite import *

FILE_PATH = 'MultipleChoiceQuestions.txt'

LETTERS_LIST = ['a', 'b', 'c', 'd']

fileHandle = openFileForReading(FILE_PATH)
titleText = ReadALine(fileHandle)

nQuestions = ReadALine(fileHandle)
nQuestions = int(nQuestions)

print("Welcome!  This test is: ")
print()
print(titleText)
print()
print("There will be ", nQuestions, "questions.")
print()
print("Let's go....")
print()

score = 0

for questionNumber in range(0, nQuestions):
    questionText = ReadALine(fileHandle)

    answers =[]
    for i in range(0, 4):
        thisAnswer = ReadALine(fileHandle)
        answers.append(thisAnswer)
        correctAnswer = answers[0]
        random.shuffle(answers)
        indexOfCorrectAnswer = answers.index(correctAnswer)
    print(str(questionNumber + 1) + '. ' + questionText)
    for index in range(0, 4):
        thisLetter = LETTERS_LIST[index]
        thisAnswer = answers[index]
        thisAnswerLine = '' + thisLetter + ' ' + thisAnswer
        print(thisAnswerLine)

    print()

    while True:
        userAnswer = input('Your answer (a, b, c, d): ')
        userAnswer = userAnswer.lower()
        if userAnswer in LETTERS_LIST:
            break
        else:
            print("Please ENTER a, b, c, or d")

    if indexOfCorrectAnswer == userAnswer:
        score = score + 1
        print('Correct!!')
    else:
        print("Sorry, that's not it mate.")
        correctLetter = LETTERS_LIST[indexOfCorrectAnswer]
        print("the correct answer is: ", + correctLetter + '' + correctAnswer)
    print()
    print("you score is: ", score)

pctCorrect = (score * 100)/ nQuestions
print()
print("All done! \nYou got", str(pctCorrect) + '% correct')

closeFile(fileHandle)
