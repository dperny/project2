from word import Word
from wordfrequency import *

class WordCloud:
    def __init__(self,count,frequency,stop_words):
        self._min = frequency.minimum()
        self._max = frequency.maximum()
        self._words = self._wordbuilder(count,frequency,stop_words)
    
    def _wordbuilder(self,count,frequency,stop_words):
        words = frequency.words()
        outwords = []
        i = 1
        count += 1
        while i <= count:
            if words[-i] not in stop_words:
                outwords.append(Word(words[-i],frequency.frequency(words[-i])))
                i += 1
            else:
                i += 1
                count += 1
        return outwords
    
    def save(self,filename):
        outstring = ''
        for word in self._words:
            outstring = outstring + str(word) + "\n"
        with open(filename,'w') as fp:
            fp.write(outstring)

class HtmlWordCloud(WordCloud):
    def __init__(self,count,frequency,stop_words):
        super(HtmlWordCloud,self).__init__(count,frequency,stop_words)
    
    # override
    def save(self,filename):

        outstring = "<html><body><table>"
        for word in self._words:
            outstring = outstring + self._htmlize(word)
        outstring = outstring + "</table></body></html>"
        with open(filename,'w') as fp:
            fp.write(outstring)
    
    def _htmlize(self,word):
        return '<tr><td style="font-size:' + str(word.size) + '">' + word.text + "</td></tr>"
