#Ex 10.3
import string

lst = list()
count = 0
dict = dict()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            count += 1
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1

for key, value in list(dict.items()):
    lst.append((value, key))

lst.sort(reverse=True)

for key, value in lst:
    print(key, value)
    
