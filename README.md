<h2>Cambridge Vocabulary list</h2>
<p>open Source project to get words from  "words.pdf" and convert it to "words.json".</p>
<p>Code discovered 99% of words inside "words.pdf"</p>
<h3>Project Structure:</h3>
<li>
words directory contain 3 files
</li>
<li>
main.py contain all codes to make that happen
</li>
<h4>Words directory:</h4>
<li>"extract-words-from-pdf.txt" contain all words and repeating words in "words.pdf"</li>
<li>"cleaned.txt" contain all words without repeating and ordered form words in "extract-words-from-pdf.txt"</li>
<li>"words.json" contain all words in json format with matching character with own words  example:{'a':['and',......,'amazing'],'b':['bulb',.......],.......etc}</li>
<p>Usage: using json file in making guess word games and get data to use it in IR systems</p>
<p>I used pycharm community edition to create this project by the power of Python 3.8.1</p>
<p>Notes: install PyPDF2 library to play with any pdf file</p>
<p>final words, I know that code is not perfect and code cant get all the words from "words.pdf",you can forked the code and play with it as much you need.</p>
