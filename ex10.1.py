#Ex 10.1
fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print("File error cannot open")
    fhand = open('mbox-short.txt')

persons = dict()
lst = list()

for lines in fhand:
    words = lines.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        person = words[1]
        persons[person] = persons.get(person, 0) + 1

for key,value in persons.items() :
    lst.append( (value, key) )

lst = sorted(lst, reverse=True)
print(lst)
print('Most comments by:', lst[0])
