class Page:
    def __init__(self, id, ins, outs):
        self.id = id
        self.ins = ins
        self.outs = outs
        self.rank = 1

def calc(pages, iters=100, damp=0.85):
    for i in range(iters):
        for (docId, page) in pages.items():
            sums = 0
            for ii in page.ins:
                sums += pages[ii].rank / len(pages[ii].outs)
            page.rank = 1 - damp + damp * sums
    sums = 0
    for (docId, page) in pages.items():
        print('%s: %s'%(docId, page.rank))
        sums += page.rank
    print('sum: %s'%sums)

count = int(input("number of pages: "))
pages = {}
for i in range(count):
    docId = input("id for page %d: "%(i+1))
    pages[docId] = Page(docId, [], [])

linkCount = int(input('numbers of links: '))
for i in range(linkCount):
    [out, to] = input('from and to: ').split(' ')
    pages[out].outs.append(to)
    pages[to].ins.append(out)
print()
calc(pages)
