import re

"""def normalize(file):
    newfile = open('cleantweets.txt', 'w')
    for line in file:
        line = re.sub('[^a-zA-Z0-9\n\.]', ' ', line)
        newfile.write(line)"""

def remove_at_symbol(file):
    outfile = open("cleatweets.text", 'w')
    for line in file:
        line = line.replace('@', '')
        outfile.write(line)
        
    