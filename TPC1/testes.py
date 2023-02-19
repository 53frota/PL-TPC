
import csv
with open('Data/myheart.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    ll=[[]]
    i=0
    j=0
    for row in spamreader:
        l = list(', '.join(row))

        ll.append(l)
       

              
print (row)





