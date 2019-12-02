import numpy as np 

count = int(input())
rels = [int(s) for s in input().split(' ')]
matched = 0
relevants = sum([0 if r == 0 else 1 for r in rels])
precisions = []
recalls = []

for i in range(count):
    if rels[i] != 0:
        matched += 1
    precisions.append(matched / (i + 1))
    recalls.append(matched / relevants)
print(precisions)
print(recalls)

bestPres = []
for pres in precisions[::-1]:
    if len(bestPres) == 0 or bestPres[-1] < pres:
        bestPres.append(pres)
    else:
        bestPres.append(bestPres[-1])
bestPres = bestPres[::-1]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()
plt.title("PR Curve")

plt.xlabel("recall")
plt.ylabel("precision");

ax.set_ylim([-0.1, 1.1])
ax.scatter(recalls, precisions)
ax.plot(recalls, bestPres)
plt.show()
