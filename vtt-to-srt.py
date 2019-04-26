import sys
import codecs
import os.path

filename = sys.argv[1]

with open(filename, encoding='utf8') as f:
    sub = [x.strip() for x in f.readlines() if 'WEBVTT' not in x]

while (not sub[0]):
    del sub[0]


def is_time_row(x):
    return '-->' in x and x.count(':') == 4 and x.count('.') == 2


index = 0
subno = 0
n = len(sub)

while (index < n):
    if is_time_row(sub[index]):
        sub[index] = sub[index].replace('.', ',')
        sub.insert(index, str(subno))
        index += 1
        subno += 1
        n += 1
    index += 1


with codecs.open(os.path.splitext(filename)[0] + '.srt', 'w', 'utf-8') as f:
    for row in sub:
        f.write(f'{row}\n')

