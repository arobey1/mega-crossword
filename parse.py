import collections

def main():

    fname = 'stuff.txt'
    outfname = 'output.txt'
    size = 50
    data = readInPuzzle(fname)
    across = getWords(data, size)

    m = createMat(data, size)
    t = map(list, zip(*m))
    d_data = ""
    for ls in t:
        d_data += "".join(ls)
    downs = getWords(d_data, size)

    all_words = across + downs
    repeats =  [item for item, count in collections.Counter(all_words).items() if count > 1]

    print "Across length: %d" % len(across)
    print "Down length: %d" % len(downs)
    print ""

    for wd in repeats:
        print wd
        print [i for i in range(len(all_words)) if all_words[i] == wd]
        print ""


    print("Total number of completed words: %d" % len(all_words))

    writeFile(all_words, outfname)

    lengths = [len(w) for w in all_words]
    avg = sum(lengths) / float(len(lengths))
    print "Average word length: %.2f" % avg

def readInPuzzle(fname):
    alldata = []
    with open(fname, 'r') as f:
        for line in f:
            alldata.append(line.strip())

    return alldata[0]

def getWords(data, size):
    valid_words = []
    for i in range(size):
        current_row = data[i * size: (i+1) * size]
        for wd in current_row.split('.'):
            if wd and '-' not in wd:
                valid_words.append(wd)

    return valid_words

def createMat(data, size):

    lines = []
    for i in range(0, size * size + 1, size):
        tmp = []
        curr = data[i : i + size]
        for j in range(len(curr)):
            tmp.append(curr[j])
        lines.append(tmp)
        tmp = []

    lines.pop()
    return lines

def writeFile(all_words, fname):
    with open(fname, 'w') as f:
        for wd in all_words:
            f.write(wd)
            f.write('\n')


main()
