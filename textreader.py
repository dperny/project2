class TextReader():

    def __init__(self, filename):
        self._filename = filename
        self._position = 0
        self._whitespace = [' ','\n','\t','\r']


    def get_word(self):
        word = ""

        with open(self._filename) as infile:
            infile.seek(self._position)
            while True:
                char = infile.read(1)
                if char == '':
                    return None
                self._position += 1
                if char in self._whitespace:
                    break
                else:
                    word = word + char

        word = word.strip('!"\,.;')
        if word == "": word = self.get_word() 

        return word
