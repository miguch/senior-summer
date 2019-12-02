import numpy as np

def vectorize(docs):
    vocab = list(set([word for doc in docs for word in doc.split(' ')]))
    mat = np.zeros((len(docs), len(vocab)))
    for i in range(len(docs)):
        for word in docs[i].split(' '):
            mat[i, vocab.index(word)] = 1
    return mat, vocab

def query_vectorize(query, vocab):
    vec = np.zeros((len(vocab), 1))
    for word in query.split(' '):
        if word in vocab:
            vec[vocab.index(word)] = 1
    return vec

def to_markdown(vec, vocab):
    title = '|'.join(['', ' ', *vocab, ''])
    sep = '|'.join(['', *[' --- ' for i in range(len(vocab)+1)], ''])
    doc_rows = []
    row, col = vec.shape
    for r in range(row):
        doc_rows.append('|'.join(['', 'doc%d'%(r+1), *[str(int(vec[r, c])) for c in range(col)], '']))
    return '\n'.join([title, sep, *doc_rows])


if __name__ == "__main__":
    count = int(input())
    docs = [input() for i in range(count)]
    vec, vocab = vectorize(docs)
    print(to_markdown(vec, vocab))
