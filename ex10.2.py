#Ex 10.2
name = input('Enter File: ')
if len(name) < 1 :
     name = 'mbox-short.txt'
handle = open(name)

hrscount = dict()
hlst = []

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] =='From' :
        hr = words[5].split(':')
        hrscount[hr[0]] = hrscount.get(hr[0], 0) + 1
    else:
        continue

for k, v in hrscount.items():
    hlst.append((k, v))

hlst.sort()
for k, v in hlst:
    print(k, v)
