class Word:
    def __init__(self,text,size):
        self.text = text
        self.size = size
        
    def __str__(self):
        return self.text+":"+str(self.size)