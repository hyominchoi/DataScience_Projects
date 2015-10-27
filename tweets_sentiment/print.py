import urllib
import json


    
for line in open('output1.txt','r').readlines():
    current_line = json.loads(line)
    if current_line.has_key("entities"):
        if (current_line["entities"]["hashtags"]!= [] ):
            for n in range(len(current_line["entities"]["hashtags"])):
                print current_line["entities"]["hashtags"][n]["text"]
            


        
        