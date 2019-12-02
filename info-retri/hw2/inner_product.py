from vectorizer import *

if __name__ == "__main__":
    count = int(input())
    docs = [input() for i in range(count)]
    vec, vocab = vectorize(docs)
    try:
        while True:
            query = input()
            query_vec = query_vectorize(query, vocab)
            print(vec.dot(query_vec))
    except EOFError:
        pass
