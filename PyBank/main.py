# Modules
import os
import csv

def printConsoleResult(totalMonth,totalNetAmount, averageChange, greatestProfit,greatestDecrease ):
    print('Financial Analysis ')
    print("-------------------------------")
    print('Total Months: ', totalMonth)
    print('Total: $', totalNetAmount)
    print('Average  Change: $', averageChange)
    print('Greatest Increase in Profits: ', greatestProfit)
    print('Greatest Decrease in Profits: ', greatestDecrease)

def getDifferntialList(listPL):
    differntialList=[]
    i=1
    while(i<len(listPL)):
        differntialList.append(listPL[i]-listPL[i-1])
        i+=1
    return differntialList

def getAverageChange(diffList):
    sum=0
    for item in diffList:
        sum=sum+item
    average= sum/len(diffList)
    return round(average,2)

totalMonth=0
totalNetAmount=0
listPL=[]
diffList=[]
allRows=[]
with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        totalMonth+=1
        totalNetAmount+=int(row[1])
        listPL.append(int(row[1]))
        allRows.append(row)
    diffList=getDifferntialList(listPL)
    greatestProfit = max(diffList)
    greatestLoss=min(diffList)
    greatestProfitMonthIndex= diffList.index(greatestProfit)+1
    greatestLossMonthIndex= diffList.index(greatestLoss)+1
    var1= (allRows[greatestProfitMonthIndex][0])+'($ '+str(greatestProfit)+')'
    var2= (allRows[greatestLossMonthIndex][0])+'($ '+str(greatestLoss)+')'

printConsoleResult(totalMonth,totalNetAmount,getAverageChange(diffList),var1,var2)
