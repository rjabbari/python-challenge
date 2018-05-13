#incorporate the os and csv modules to be read
import os
import csv

#create a path for the files to be used
bank_csv_path = os.path.join("resources", "budget_data_2.csv")

#to hold the list of values
date_list=[]
rev_list=[]
change_list=[]

with open(bank_csv_path,newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader=csv.reader(csvfile,delimiter=",")

    #counts the number of rows with data; skippin the fist row
    next(csv_reader)
    csv_reader = list(csv_reader)
    count = len(csv_reader)

    #sum up the revenue column
    total = sum(int(mylist[1]) for mylist in csv_reader)

    for i in csv_reader:
        date_list.append(str(i[0]))

    for i in csv_reader:
        rev_list.append(float(i[1]))

    for i in range(0,len(rev_list)-1):
        change_list.append(rev_list[i+1]-rev_list[i])

    for j in change_list:
        ave_diff=sum(change_list)/len(change_list)

print('Total Months: '+ str(count))
print('Total Revenue: '+ str(round(total,2)))
print("Average Revenue Change: "+str(round(ave_diff,2)))
print("Greatest Increase in Revenue: "+ str(max(change_list)))
print("Greatest Decrease in Revenue: "+ str(min(change_list)))
