import csv
with open('Data/myheart.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    ll=[[]]
    for row in spamreader:
        l = list(', '.join(row))
        ll.append(l)
    print(ll)




