#simple money saving app redux ver 2.3

import datetime
import calendar

date = datetime.datetime.now()

#finds how many days are in the current month and year (accounts for leap year)
currentMonth = date.month
currentYear = date.year
currentDay = date.day


#gets how many days there are in the month
days = calendar.monthrange(currentYear,currentMonth)[1]

#main function of the applicaton
budget = float(input("what is your budget for this month? \nOnly in whole $ amounts: $"))
dailySpend = round(budget/days, 2)
print(f"you can only spend ${dailySpend} a day to stay in budget")

daysInMonth = [] #store how many days in month in a list to convert to a dictionary later
count = 0 #use to create the list for daysInMonth
while count != days:
    daysInMonth.append(count +1)
    count +=1


dailyBudget = {} #creates a dictionary (key:val pair) for the allowed daily spend 
for day in daysInMonth:
    dailyBudget[day] = dailySpend


startOfMonth =1 #calculates the previous day's budget to be added to the current day
while startOfMonth != currentDay:
    dailyBudget[currentDay] = dailyBudget[currentDay] + dailyBudget[startOfMonth]
    dailyBudget[startOfMonth] = 0
    startOfMonth +=1


#shows user how much is allowed to spend for the day
myBudget = str(round(float(dailyBudget[currentDay]),2))
print(f"Your balance as of today is ${myBudget}")

#deducts from daily budget
amountSpent = (round(float(input("Please enter the amount spent today: $")),2))
dailyBudget[currentDay] = dailyBudget[currentDay] - amountSpent

#checks if balance is less than 0
if dailyBudget[currentDay] < 0:
    print("hey bud you fucked up and spent too much, FUCKING LOSER")#----------------MY PERSONAL TEST---------------#
    lockOut = dailyBudget[currentDay]

    dayCounter = 0
    while lockOut <0:
        dayCounter += 1
        lockOut = lockOut + dailySpend

    print(f"You have to wait {dayCounter} days before you are able to spend more")
    
currentBalance = round(float(dailyBudget[currentDay]),2)
#tests
print(f"Your current balance ${currentBalance}")
#print(dailyBudget)