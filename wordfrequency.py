from textreader import *
import operator

class WordFrequency():
    
    def __init__(self):
        self._words = {}

    def open(self,filename):
        reader = TextReader(filename)
        word = reader.get_word()
        while word is not None:
            if word in self._words:
                self._words[word] += 1
            else:
                self._words[word] = 1
            word = reader.get_word()

    def frequency(self,word):
        if word in words:
            return words[word]
        else:
            return -1

    def maximum(self):
        return max(self._words.iteritems(),key=operator.itemgetter(1))[0]

    def minimum(self):
        return min(self._words.iteritems(),key=operator.itemgetter(1))[0]

    def words(self):
        return sorted(self._words.keys())

    def save(self,filename):

        wordslist = self.words()

        outstring = ""
        for key in wordslist:
            outstring = outstring + str(key) + ":" + str(self._words[key]) + "\n"
        
        with open(filename,"w") as outfile:
            outfile.write(outstring)
