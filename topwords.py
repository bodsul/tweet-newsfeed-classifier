import nltk
from converttweettoarray import *

#returns top 50 words from a bunch of tweets stored as a python list in a file named filename
#list most common words in english

common100 = {1: 'the', 2: 'of', 3: 'and', 4: 'a', 5: 'to', 6: 'in', 7: 'is', 8: 'you', 9: 'that', 10: 'it', 11: 'he', 12: 'was', 13: 'for', 14: 'on', 15: 'are', 16: 'as', 17: 'with', 18: 'his', 19: 'they', 20: 'i', 21: 'at', 22: 'be', 23: 'this', 24: 'have', 25: 'from', 26: 'or', 27: 'one', 28: 'had', 29: 'by', 30: 'word', 31: 'but', 32: 'not', 33: 'what', 34: 'all', 35: 'were', 36: 'we', 37: 'when', 38: 'your', 39: 'can', 40: 'said', 41: 'there', 42: 'use', 43: 'an', 44: 'each', 45: 'which', 46: 'she', 47: 'do', 48: 'how', 49: 'their', 50: 'if', 51: 'will', 52: 'up', 53: 'other', 54: 'about', 55: 'out', 56: 'many', 57: 'then', 58: 'them', 59: 'these', 60: 'so', 61: 'some', 62: 'her', 63: 'would', 64: 'make', 65: 'like', 66: 'him', 67: 'into', 68: 'time', 69: 'has', 70: 'look', 71: 'two', 72: 'more', 73: 'write', 74: 'go', 75: 'see', 76: 'number', 77: 'no', 78: 'way', 79: 'could', 80: 'people', 81: 'my', 82: 'than', 83: 'first', 84: 'water', 85: 'been', 86: 'call', 87: 'who', 88: 'oil', 89: 'its', 90: 'now', 91: 'find', 92: 'long', 93: 'down', 94: 'day', 95: 'did', 96: 'get', 97: 'come', 98: 'made', 99: 'may', 100: 'part', 101: 'new', 102: 'rt', 103: "don't", 104: '&amp;' , 105:'&amp', 106: 'uses', 107: 'makes', 108: 'need', 109: 'news', 110: 'why', 111: 'our', 112: 'wants', 113: 'even', 114: 'here', 115: '2014', 116: '/', 117:'(!)', 118: '--', 119: '-', 120: 'back', 121: 'until', 122: 'take', 123: 'year', 124: 'years', 125: 'messages', 126: 'twitter', 127: 'this,' , 128: 'wrote', 129: 'good', 130: 'bad', 131: 'them."', 132: 'things', 133: "that's", 134: 'that,', 135: 'very', 136: '(blog)', 137: "you're", 138: 'after', 139: 'via', 140: "it's", 141: 'u.s.', 142: "here's", 143: 'bbcnormans', 144: 'think' , 145: 'england', 146: '...', 147: 'today', 148: 'us', 149: 'should', 150: 'just', 151: 'really', 152: 'ways', 153: 'me', 154: 'still', 155: '+', 156: "today's", 157: 'want', 158: 'know', 159: "you'll", 160: 'any', 161: 'tweet', 162: 'every', 163:'everything', 164: 'few', 165: 'much', 166: "you've", 167: 'comments', 168: 'ask', 169:'might', 170:'most', 171: '0', 172: '1', 173: '2', 174: '3', 175: '4', 176: '5', 177: '6', 178: '7', 179: '8', 180: '9', 181: '10', 182: 'you.', 183: "we'll", 184: 'w/', 185: 'too', 186: 'r', 187: 'n', 188: 'e', 189: 'am', 190: 'uk', 191: 'thanks', 192: 'live', 193: 'retweet', 194:'retweets', 195:'try', 196: 'got', 197: "i'm", 198: 'this!', 199: 'follow', 200:'only'}



def gettop(filename):
    a = copy_to_array(filename)
    words = []
    for i in range(0,len(a)):
        words += [word for word in a[i].split()]
    
    #remove common100words
    k = 0
    for i in range(0,len(words)):
        if k >=len(words):
            break
        if words[k] in common100.values():
            words.pop(k)
            k = k-1
        k = k+1

    words_ranked = nltk.FreqDist(words)
    words =[]

    for key, value in sorted(words_ranked.items(), key = lambda item: (item[1], item[0])):
        words.append(key)

    return words[-50:]