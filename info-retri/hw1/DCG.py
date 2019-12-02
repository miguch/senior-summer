import numpy as np 
count = int(input())
sums = 0
res = []
rels = []
for i in range(count):
    rels.append(float(input()))
for (i, rel) in enumerate(rels):
    if i == 0:
        sums += rel
    else:
        sums += rel / np.log2(i+1)
    res.append(sums)
print(res)
