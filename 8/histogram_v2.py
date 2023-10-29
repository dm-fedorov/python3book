# histogram_v2.py
def histogram(s):
    word_count = {}
    for word in s:
        word_count.setdefault(word, 0)  
        word_count[word] += 1        
    return word_count
