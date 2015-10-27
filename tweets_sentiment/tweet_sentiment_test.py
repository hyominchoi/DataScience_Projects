import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    for line in open(sys.argv[2],'r').readlines():
        current_line = json.loads(line)
        line_score = 0
        if current_line.has_key("text"):
            tweet_text = current_line ["text"]
            for word in tweet_text.split():
                #print word
                if scores.has_key(word):
                    line_score = line_score + scores[word]
                else:
                    line_score = line_score
            print line_score
           # print current_line["text"]
     
       
            
        
    
if __name__ == '__main__':
    main()
