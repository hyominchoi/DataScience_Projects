import sys
import json
from sys import stdout

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    extra = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items()    
    for line in open(sys.argv[2],'r').readlines():
        current_line = json.loads(line)
        line_score = 0
        if current_line.has_key("text"):
            tweet_text = current_line ["text"]
            for word in tweet_text.split():
                #print word
                if scores.has_key(word):
                    line_score = line_score + scores[word]
                elif extra.has_key(word):
                    line_score = line_score
                    extra[word][1]=extra[word][1]+1
                elif len(word)>2 :  
                    extra[word] = [0,1]
                    line_score = line_score 
                else: 
                    line_score = line_score
            for word in tweet_text.split():
                if (extra.has_key(word) and line_score>0 ):
                    extra[word][0] = extra[word][0] + 1
                elif (extra.has_key(word) and line_score<0) :
                    extra[word][0] = extra[word][0] - 1
    for x in extra:
        y = float(extra[x][0])/float(extra[x][1]) 
        print x,; print y

       
         
 
if __name__ == '__main__':
    main()
