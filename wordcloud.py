from word import Word
from wordfrequency import *
import math
from copy import copy
import random

class WordCloud:
    def __init__(self,count,frequency,stop_words):
        self._min = frequency.frequency(frequency.minimum())
        self._max = frequency.frequency(frequency.maximum())
        self._count = count
        self._words = self._wordbuilder(count,frequency,stop_words)
    
    def _wordbuilder(self,count,frequency,stop_words):
        words = frequency.words()
        outwords = []
        i = 1
        count += 1
        while i <= count:
            if words[-i] not in stop_words:
                freq = frequency.frequency(words[-i])
                outwords.append(Word(words[-i],freq))
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

        outlist = ["<html><body><table>"]
        words = copy(self._words)
        random.shuffle(words)
        cols = math.floor(self._count/math.e)
        i = 0
        for word in words:
            if i % cols == 0 and i != 0:
                outlist.append("</tr>")
                outlist.append("<tr>")
            elif i == 0:
                outlist.append("<tr>")
            outlist.append(self._htmlize(word))
            i += 1
        outlist.append("</table></body></html>")
        outstring = "".join(outlist)
        with open(filename,'w') as fp:
            fp.write(outstring)
    
    def _htmlize(self,word):
        fmax = 72
        size = (fmax*(word.size - self._min))/(self._max - self._min)
        return '<td align="center" style="font-size:' + str(size) + '">' + word.text + "</td>"
