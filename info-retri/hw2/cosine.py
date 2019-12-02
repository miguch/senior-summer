from vectorizer import *
import numpy as np

if __name__ == "__main__":
    count = int(input())
    docs = [input() for i in range(count)]
    vec, vocab = vectorize(docs)
    try:
        while True:
            query = input()
            query_vec = query_vectorize(query, vocab)
            print((np.linalg.norm(vec, axis=1) * np.linalg.norm(query_vec)))
            print(vec.dot(query_vec) / (np.linalg.norm(vec, axis=1).reshape(-1, 1) * np.linalg.norm(query_vec)))
    except EOFError:
        pass
