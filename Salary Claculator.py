#This program will calculate the amount of money a person would earn over a period of time exponentially from $0.01
#Pedro Ayala

#User input for the number of days
numDays = int(input("Enter the number of days you are being paid for: $"))

multiplier = 1  #Initialize multiplier to 1
total = 0       #Initialize total to 0

#Loop to calculate and display the salary
for i in range(1, numDays + 1):
    print ("Day: ", i, "salary: $", multiplier / 100)     #display day and salary
    multiplier = multiplier * 2                           #multiplier variable to double salary each day
    total = total + multiplier                            #total accumulator

#calculations for the total in dollars
total = total / 2

#Display total amount earned
print ("The total amount of money earned is: $", total / 100)
