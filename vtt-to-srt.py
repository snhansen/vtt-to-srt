import sys
import codecs

filename = sys.argv[1]

with open(filename,encoding='utf8') as f:
    sub = [x.strip() for x in f.readlines() if 'WEBVTT' not in x]

while (not sub[0]):
    del sub[0]
    
def istimerow(x):
    return ('-->' in x) & (x.count(':') == 4) & (x.count('.') == 2)

index = 0
subno = 0
n = len(sub)

while (index < n):
    if istimerow(sub[index]):
        sub[index] = sub[index].replace('.',',')
        sub.insert(index,str(subno))
        index += 1
        subno += 1
        n += 1
    index += 1

with codecs.open(filename.split('vtt')[0] + 'srt', 'w', 'utf-8') as f:
    for row in sub:
        f.write("%s\n" % row)
