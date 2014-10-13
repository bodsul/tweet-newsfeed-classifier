from unidecode import unidecode

class TWIT:
    'class holding array of tweets'
    def __init__(self, a):
        self.a = a
    
    def clean(self):
        for i in range(0, len(self.a)):
            x = self.a[i].split()
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
            self.a[i] = ' '.join(x)
            self.a[i] = self.a[i].lower()

    def display(self):
        print self.a

    