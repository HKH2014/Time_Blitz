import csv

def sorting_data(sort):
    if len(sort) > 1:
        #if the data in the list is 1 then its already sorted
        left_side = sort[:len(sort)//2]
        right_side = sort[len(sort)//2:]
        #these two create the notation to get parts of an array
        #here i'm literally dividing the array in half
        #:len begins at the 1st element - index o, //2: is the ending index
        #this list can take any number of values, useful as there can be an unlimited number of users
        #merge sort constantly splits a list in half until the list has 1 value in it
        sorting_data(left_side)
        sorting_data(right_side)
        L = 0
        R = 0
        M = 0 # the final merged array
#its a recursive process so continue to use while until it reaches the 1 value
        while L < len(left_side) and R < len(right_side):
            #while the left list has more elements in it than 0
            #while right list has more elements in it than 0
            if left_side[L] < right_side[R]:
                sort[M] = left_side[L]
                #can save whatever is in our left array into our merged array
                L = L + 1
            else: #same thing occurs but with the right side
                sort[M] = right_side[R]
                R = R + 1
            M = M + 1
            #increment the merge sort when list has been divided
            # We ran out of elements either in left_side or right_side, so we will go through the remaining elements and add them
        while L < len(left_side):
             sort[M] = left_side[L]
             L = L + 1#just increase single indexes
             M = M + 1
        while R < len(right_side):
             sort[M] = right_side[R]
             R = R + 1
             M = M + 1


ask1 = input("Enter first user number:")
ask1_int = int(ask1)
ask2 = input("Enter second user number, press enter to move on:")
ask2_int = int(ask2)
ask3 = input("Enter third user number, press enter to move on:")
ask3_int = int(ask3)
with open('UserDetails.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        Q = (row[ask1_int],row[8])
        R = (row[ask2_int],row[8])
        S = (row[ask3_int],row[8])
        data [Q,R,S]

#data = [5,4,3,2,1]
sorting_data(data)
print(data)

     
