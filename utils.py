def getLen(string):
    return len(string)

def standartdized(string):
    s=string.lower()        
    s = ' '.join(s.split()) # Loai bo khoang trang thua
    return s 

def count(string):
    c = len(string.split()) 
    return c
