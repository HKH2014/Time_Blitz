import csv

score = 12

print("Total score: " , score )

#This paragraph is to update the database with the new score irregardless of the old score
UserInfo = open('UserDetails.csv', 'r') # I need to read the rows to find the score section
reader = csv.reader(UserInfo)# to make things easier I'm just going to save these attributes under a single variable
TheInfo = list(reader)
UserInfo.close()
TheInfo[2][8] = score # I'm spesifying a cell and re-writing the data to whatever new score the player has gotten
my_new_list = open('UserDetails.csv', 'w', newline = '')
csv_writer = csv.writer(my_new_list)
csv_writer.writerows(TheInfo)
my_new_list.close()

print("Compare your scores with others!")
# This section  here prints every score saved on the database alongside the owners ID (GDPR doesn't allow names i dont think?)
with open('UserDetails.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        #objetive - organising scores from lowest to highest
       #print(ord(row['ID'], row['Score']
        #This doesn't work because the whole leader board is transferred as a single variable so I can't order the values in them
        #However, since all the scores are shown, children can rank them themselves if they want to.
#check and see if sorted works
        p = 7,3,9,2
        print(sorted(p))
        f = row['Score']
        print(sorted(f))
        print(sorted(row['ID'], "has a score of " ,  row['Score']))
       
