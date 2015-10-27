import sys
import json
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    tweet_file = open(sys.argv[1])
    hashtags = {} #Initialize top_ten dictionary
    for line in open(sys.argv[1],'r').readlines():
        current_line = json.loads(line)
        if current_line.has_key("entities"):
            if (current_line["entities"]["hashtags"]!= [] ):
                tweet_hashtag_list = current_line["entities"]["hashtags"]
                for n in range(len(tweet_hashtag_list)):
                    word = tweet_hashtag_list[n]["text"]   
                    if hashtags.has_key(word): 
                        hashtags[word] = hashtags[word] + 1
                    else:
                        hashtags[word] = 1
       
    top_ten = sorted(hashtags.iteritems(), key=operator.itemgetter(1))  
    for i in range (10):
        print top_ten[ -1 -i][0],; print float(top_ten[-1-i][1])
    
if __name__ == '__main__':
    main()        