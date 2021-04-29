# python default library
import re
import os
import json
import string
# third party library to play with pdf files
import PyPDF2

stemWords = ["abbrev", "adj", "adv", "av", "Am", "Eng", "Br", "conj", "det", " exclam", "mv", "n", "phrv", "pi",
             "prep",
             "prep", "phr" "pron", "sing", "v"]


# create "words directory" in root of project
def createDirectory():
    wordsDirectory = "words directory"
    root_dir = os.path.abspath(os.curdir)
    pathWordsDirectory = os.path.join(root_dir, wordsDirectory)
    if not os.path.exists(pathWordsDirectory):
        os.mkdir(pathWordsDirectory)


# path manipulation for files
def FilePathWords(filename, wordsDirectory="words directory"):
    root_dir = os.path.abspath(os.curdir)
    pathWordsDirectory = os.path.join(root_dir, wordsDirectory)
    pathFileWord = os.path.join(pathWordsDirectory, filename)
    return pathFileWord


# open words.pdf return as object
def pdfReaderFunction():
    pdfFileObj = open('words.pdf', 'rb')
    return PyPDF2.PdfFileReader(pdfFileObj)


# take page pdf Content and cleaned it
def wordCleaner(pageContent):
    pageContentWord = []
    for word in pageContent:
        cleanedWords = []
        findNewLine = word.find('/n')
        if findNewLine > -1:
            word = word.replace('/n', '')
        findDivideSymbol = word.find('/')
        if findDivideSymbol > -1:
            cleanedWords = word.split('/')
        else:
            cleanedWords.append(word)
        for wordClean in cleanedWords:
            wordClean = regex.sub('', wordClean)
            if wordClean != "" and len(wordClean) > 1 and wordClean not in stemWords:
                pageContentWord.append(wordClean)
    return pageContentWord


# clean Documents and delete duplicates
def cleanDocument(pathFileWord):
    contentWordsTxt = open(pathFileWord, 'r')
    listStringFile = contentWordsTxt.readline().lower().split(" ")
    listStringFile.sort()
    removeDuplicateWord = []
    [removeDuplicateWord.append(word) for word in listStringFile if word not in removeDuplicateWord]
    return " ".join(removeDuplicateWord)


# Generate file content all unique words
def cleanFileTxt(stringsJoined):
    cleanedFilePath = FilePathWords("cleanedFile.txt")
    cleanedFile = open(cleanedFilePath, 'w')
    cleanedFile.write(stringsJoined)
    cleanedFile.close()


# create dictionary contain 'a':[] ,'b:[]....etc
def createDictionaryChar():
    dicWords = {}
    for index in string.ascii_lowercase:
        dicWords[index] = []
    return dicWords


if __name__ == '__main__':
    createDirectory()
    pathFileWords = FilePathWords("extract-words-from-pdf.txt")
    regex = re.compile('[^a-zA-Z]')
    pdfReader = pdfReaderFunction()
    for pageIndex in range(4, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageIndex)
        openFileWords = open(pathFileWords, "a")
        pageContents = pageObj.extractText().split(" ")
        pageContentWords = wordCleaner(pageContents)
        pageContentWords.sort()
        oneWordPerPage = {}
        for index in pageContentWords:
            oneWordPerPage[index] = 1
        openFileWords.write(" ".join(oneWordPerPage.keys()))
        openFileWords.close()

    stringJoined = cleanDocument(pathFileWords)
    cleanFileTxt(stringJoined)

    dicWord = createDictionaryChar()

    loadStringJoined = open(FilePathWords("cleanedFile.txt"))
    extractString = loadStringJoined.readline().split(" ")

    for word in extractString:
        dicWord[word[0]] = [word] + dicWord[word[0]]
    jsonWord = json.dumps(dicWord, indent=4)

    jsonFile = open(FilePathWords("words.json"), "w")
    jsonFile.write(jsonWord)
    jsonFile.close()
