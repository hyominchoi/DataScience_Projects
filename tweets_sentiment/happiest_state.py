import sys
import json
import operator
from types import *
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    keys = states.keys()
    frequency = {key:0 for key in keys}
    happiness = {key:0 for key in keys}
    
    scores = {} # initialize an empty dictionary
    afinnfile = open(sys.argv[1])
    for line in afinnfile:
        
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
   
   
    for line in open(sys.argv[2],'r').readlines():
        
        current_line = json.loads(line)
        line_score = 0
        
        if (current_line.has_key("text") and current_line.has_key("place")):
            tweet_text = current_line["text"]
            tweet_place = current_line["place"]
            
            if(type(tweet_place) is DictType and tweet_place["country_code"]=="US"):
                city, state = tweet_place["full_name"].split(", ")
                state = str(state)
                if (len(state) == 2):
                    frequency[state] = frequency[state] + 1
                    for word in tweet_text.split():
                        if scores.has_key(word):
                            line_score = line_score + scores[word]
                        else:
                            line_score = line_score
                    happiness[str(state)] = happiness[str(state)] + line_score
                       
                 
    for key in happiness:
        if (frequency[key] != 0):
            happiness[key] = float(happiness[key])/float(frequency[key])
        
    happiest_state = sorted(happiness.iteritems(), key=operator.itemgetter(1))    
    
    print happiest_state[-1][0]
            
           # print current_line["text"]

    

    
if __name__ == '__main__':
    main()        