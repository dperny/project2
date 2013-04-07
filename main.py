import sys
from wordfrequency import *
from textreader import *

def main(args):
    Freq = WordFrequency()

    for arg in args[1:]:
        Freq.open(arg)

    Freq.save("freq.dat")

if __name__ == "__main__":
    main(sys.argv)
