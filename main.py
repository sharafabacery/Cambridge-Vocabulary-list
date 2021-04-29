import re
import os
import json
import string
import PyPDF2

stemWords = ["abbrev", "adj", "adv", "av", "Am", "Eng", "Br", "conj", "det", " exclam", "mv", "n", "phrv", "pi",
             "prep",
             "prep", "phr" "pron", "sing", "v"]


def createDirectory(fileName):
    wordsDirectory = "words directory"
    root_dir = os.path.abspath(os.curdir)
    pathWordsDirectory = os.path.join(root_dir, wordsDirectory)
    pathFileWord = os.path.join(pathWordsDirectory, fileName)
    if not os.path.exists(pathWordsDirectory):
        os.mkdir(pathWordsDirectory)
    return pathFileWord


def pdfReaderFunction():
    pdfFileObj = open('words.pdf', 'rb')
    return PyPDF2.PdfFileReader(pdfFileObj)


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


def cleanDocument(pathFileWord):
    contentWordsTxt = open(pathFileWord, 'r')
    listStringFile = contentWordsTxt.readline().lower().split(" ")
    listStringFile.sort()
    removeDuplicateWord = []
    [removeDuplicateWord.append(word) for word in listStringFile if word not in removeDuplicateWord]
    return " ".join(removeDuplicateWord)


def cleanFileTxt(stringsJoined):
    cleanedFilePath = createDirectory("cleanedFile.txt")
    cleanedFile = open(cleanedFilePath, 'w')
    cleanedFile.write(stringsJoined)
    cleanedFile.close()


if __name__ == '__main__':
    pathFileWords = createDirectory("extract-words-from-pdf.txt")
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

    jsonWord = {}
    for i in string.ascii_lowercase:
        jsonWord[i] = []
    loadStringJoined = open(createDirectory("cleanedFile.txt"))
    extractString = loadStringJoined.readline().split(" ")
    for word in extractString:
        jsonWord[word[0]] = [word] + jsonWord[word[0]]
    json_object = json.dumps(jsonWord, indent=4)

    # Writing to sample.json
    with open(createDirectory("words.json"), "w") as outfile:
        outfile.write(json_object)
