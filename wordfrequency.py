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
        if word in self._words:
            return self._words[word]
        else:
            return -1

    def maximum(self):
        return self.words()[-1] 

    def minimum(self):
        return self.words()[0] 

    def words(self):
        rlist = sorted(self._words.items(),key=operator.itemgetter(1))
        return [i[0] for i in rlist]

    def save(self,filename):

        wordslist = self.words()

        outstring = ""
        for key in wordslist:
            outstring = outstring + str(key) + ":" + str(self._words[key]) + "\n"
        
        with open(filename,"w") as outfile:
            outfile.write(outstring)
