import numpy as np 

def getDCG(rels, count):
    sums = 0
    res = []
    for i in range(count):
        rel = rels[i]
        if rel != 0:
            if i == 0:
                sums += rel
            else:
                sums += rel / np.log2(i+1)
        res.append(sums)
    return res

count = int(input())
rels = [float(s) for s in input().split(' ')]
ideal = sorted(rels, reverse=True)
dcg = getDCG(rels, count)
truth = getDCG(ideal, count)
print(rels[:count])
print(ideal[:count])
print(dcg)
print(truth)
print(np.array(dcg) / np.array(truth))
