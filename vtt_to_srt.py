import sys
import os.path

filename = sys.argv[1]

with open(filename, encoding='utf8') as f:
    sub = [x.strip() for x in f.readlines() if 'WEBVTT' not in x]


while not sub[0]:
    del sub[0]


def is_time_row(x):
    return '-->' in x and x.count(':') == 4 and x.count('.') == 2


subno = 0
srtsub = []

for row in sub:
    if is_time_row(row):
        row = row.replace('.', ',')
        srtsub.append(str(subno) + '\n')
        subno += 1
    srtsub.append(row + '\n')

with open(os.path.splitext(filename)[0] + '.srt', 'w', encoding='utf-8') as f:
    f.writelines(srtsub)

