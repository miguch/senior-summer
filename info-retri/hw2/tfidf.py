from vectorizer import *
import numpy as np

def get_tfidf(doc, corpus):
    terms = list(set(doc.split(' ')))
    total_occur = {term: 0 for term in terms}
    for d in corpus:
        for term in terms:
            if term in d.split(' '):
                total_occur[term] += 1
    idf = {term: np.log10(len(corpus) / total_occur[term]) for term in terms}
    frequency = {term: 0 for term in terms}
    for word in doc.split(' '):
        frequency[word] += (1 / len(doc.split(' ')))
    return {term: frequency[term] * idf[term] for term in terms}

if __name__ == "__main__":
    count = int(input())
    docs = [input() for i in range(count)]
    print(get_tfidf(docs[0], docs))
    
