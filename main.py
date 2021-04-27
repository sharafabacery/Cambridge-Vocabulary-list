import re
import os
import PyPDF2

if __name__ == '__main__':
    ll = ["abbrev", "adj", "adv", "av", "Am", "Eng", "Br", "conj", "det", " exclam", "mv", "n", "phrv", "pi", "prep",
          "prep", "phr" "pron", "sing", "v"]
    words = "words directory"
    root_dir = os.path.abspath(os.curdir)
    path = os.path.join(root_dir, words)
    path1 = os.path.join(path, "extract-words-from-pdf.txt")
    if not os.path.exists(path):
        os.mkdir(path)
    regex = re.compile('[^a-zA-Z]')
    pdfFileObj = open('words.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(pdfReader.numPages):
        print(i)
        pageObj = pdfReader.getPage(i)
        f = open(path1, "a")
        txt = pageObj.extractText().split(" ")
        l = []
        for i in txt:
            pp = []
            xc = i.find('/n')
            if xc > -1:
                i = i.replace('/n', '')
            cv = i.find('/')
            if cv > -1:
                pp = i.split('/')
            else:
                pp.append(i)
            for ppp in pp:
                b = regex.sub('', ppp)
                if b != "" and len(b) > 1 and b not in ll:
                    l.append(b)

        l.sort()
        print(l)
        dict = {}
        for i in l:
            # if dict[i] is not None:
            dict[i] = 1
        print(dict.keys())
        f.write(" ".join(dict.keys()) + '\n')
        f.close()
