import json

def copy_to_array(filename):
    f = open(filename)
    a = json.load(f)
    for i in range(0, len(a)):
        a[i] = a[i].encode('utf-8')
    return a
