from word import Word
from wordfrequency import *
import math

class WordCloud:
    def __init__(self,count,frequency,stop_words):
        self._min = frequency.minimum()
        self._max = frequency.maximum()
        self._words = self._wordbuilder(frequency,count,stop_words)
    
    def _wordbuilder(self,count,frequency,stop_words):
        words = frequency.words()
        outwords = []
        i = 1
        count += 1
        while i <= count:
            if words[-i] not in stop_words:
                outwords.append(Word(words[-1],frequency.frequency(words[-i])))
                i += 1
            else:
                i += 1
                count += 1
        return outwords
    
    def save(self,filename):
        outstring = ''
        for word in self._words:
            outstring = outstring + str(word)
        with open(filename,'w') as fp:
            fp.write(outstring)

class HtmlWordCloud(WordCloud):
    # override
    def save(self,filename):
        outstring = "<html><body><table>"
        for word in self._words:
            outstring = outstring + self._htmlize(word)
        outstring = outstring = "</table></body></html>"
    
    def _htmlize(self,word):
        return '<tr><td style="font-size:' + str(math.floor(math.log(word.size))) + '">' + word.text + "</td></tr>"