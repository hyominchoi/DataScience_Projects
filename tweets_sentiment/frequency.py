import sys
import json
from sys import stdout

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    frequency = {} #initializing frequency dictionary 
    for line in open(sys.argv[1],'r').readlines():
        current_line = json.loads(line)
        if current_line.has_key("text"):
            tweet_text = current_line ["text"]
            for word in tweet_text.split():
                if frequency.has_key(word):
                    frequency[word] = frequency[word] + 1
                else :  
                    frequency[word] = 1
    y = 0 
    for key in frequency:
        y = y + frequency[key]
    
    for key in frequency:
        print key, ; print float(frequency[key])/float(y)

       
         
 
if __name__ == '__main__':
    main()
