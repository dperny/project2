import sys
from wordfrequency import *
from textreader import *
from wordcloud import *
STOP_WORDS = ["a","an","A","An","The","and","And","but","But","that","That","which","Which"]

def main(args):
    Freq = WordFrequency()

    Cloud = WordCloud(30,Freq,STOP_WORDS)
    Cloud.save("cloud.txt")
    
    HtmlCloud = HtmlWordCloud(30,Freq,STOP_WORDS)
    HtmlCloud.save("cloud.html"

if __name__ == "__main__":
    main(sys.argv)
