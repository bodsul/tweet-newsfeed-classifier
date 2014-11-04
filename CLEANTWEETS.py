#import nltk
from unidecode import unidecode

class CLEANTWEETS:
    def __init__(self, tweets):
        self.tweets = tweets
        
    def clean(self):
        "first decode none ASCII characters"
        for key in self.tweets.keys():
            a = self.tweets[key]
            for i in range(0, len(a)):
                x = a[i].split()
                x = [unidecode(b.decode('utf8')) for b in x]
                k = 0
                #break needed since if we pop from x
                for j in range(0, len(x)):
                    if (k >= len(x)):
                            break
                            
                    if('@' in x[k]):
                        x[k]=x[k].replace('@','')
                            
                    if('#' in x[k]):
                        x[k]=x[k].replace('#','')
                            
                    if('\\' in x[k]):
                        x[k]=x[k].replace('\\',"")

                    if('|' in x[k]):
                        x[k]=x[k].replace('|',"")
                            
                    if(':' in x[k]):
                        x[k]=x[k].replace(':',"")
                            
                    if (x[k].startswith('http')):
                        x.pop(k)
                        k = k-1
                    k = k+1
                a[i] = ' '.join(x)
                a[i] = a[i].lower()
            self.tweets[key] = a
        return self.tweets
