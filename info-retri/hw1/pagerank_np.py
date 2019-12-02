# import numpy as np

# def calc(pages, iters=100, damp=0.85):
#     for i in range(iters):
#         for (docId, page) in pages.items():
#             sums = 0
#             for ii in page.ins:
#                 sums += pages[ii].rank / len(pages[ii].outs)
#             page.rank = 1 - damp + damp * sums
#     sums = 0
#     for (docId, page) in pages.items():
#         print('%s: %s'%(docId, page.rank))
#         sums += page.rank
#     print('sum: %s'%sums)

# count = int(input("number of pages: "))
# pages = {}
# links = np.zeros((count, count))
# for i in range(count):
#     docId = input("id for page %d: "%(i+1))
#     pages[docId] = i

# linkCount = int(input('numbers of links: '))
# for i in range(linkCount):
#     [out, to] = input('from and to: ').split(' ')
#     links[pages[out], pages[to]] = 1
# print(count)
# for i in range(count):
#     links[i, :] /= links[i, :].sum()
# print()
# # calc(links)
