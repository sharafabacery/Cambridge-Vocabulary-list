import re
import os
import PyPDF2

stemWords = ["abbrev", "adj", "adv", "av", "Am", "Eng", "Br", "conj", "det", " exclam", "mv", "n", "phrv", "pi",
             "prep",
             "prep", "phr" "pron", "sing", "v"]

wordsDirectory = "words directory"


def createDirectory(wordDirectory, fileName):
    root_dir = os.path.abspath(os.curdir)
    pathWordsDirectory = os.path.join(root_dir, wordDirectory)
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


if __name__ == '__main__':
    pathFileWords = createDirectory(wordsDirectory, "extract-words-from-pdf.txt")
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
        openFileWords.write(" ".join(oneWordPerPage.keys()) + '\n')
        openFileWords.close()
