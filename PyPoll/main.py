# Modules
import os
import csv
import sys
import operator

def printConsoleResult(totalVotes,khanVotes, correyVotes, liVotes,otooleyVotes,winner):
    print('Election Results ')
    print("-------------------------------")
    print('Total Votes: ', totalVotes)
    print("-------------------------------")
    print(f'Khan: {khanPercentage:.3f}% ({khanVotes})')
    print(f'Correy: {correyPercentage:.3f}% ({correyVotes})')
    print(f'Li: {liPercentage:.3f}% ({liVotes})')
    print(f'O\'Tooley: {otooleyPercentage:.3f}% ({otooleyVotes})')
    print("-------------------------------")
    print('Winner: ', winner)
    print("-------------------------------")

totalVotes=0
khanVotes=0
correyVotes=0
liVotes=0
otooleyVotes=0
election_stats={}

with open('election_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        totalVotes+=1
        if(row[2]=='Khan'):
            khanVotes+=1
        elif (row[2]=='Correy'):
            correyVotes+=1
        elif (row[2]=='Li'):
            liVotes+=1
        else:
            otooleyVotes+=1
    khanPercentage= (khanVotes/totalVotes) *100
    correyPercentage= (correyVotes/totalVotes) *100
    liPercentage= (liVotes/totalVotes) *100
    otooleyPercentage= (otooleyVotes/totalVotes)*100
    election_stats={'Khan':khanVotes,'Correy':correyVotes,'Li':liVotes,'O\'Tooley':otooleyVotes}
    winner=max(election_stats.items(), key=operator.itemgetter(1))[0]

#Print the output to Console.
printConsoleResult(totalVotes,khanVotes,correyVotes,liVotes,otooleyVotes,winner)

#Redirect the output to text file.
sys.stdout=open('PyPollOutput.txt','w')
printConsoleResult(totalVotes,khanVotes,correyVotes,liVotes,otooleyVotes,winner)
