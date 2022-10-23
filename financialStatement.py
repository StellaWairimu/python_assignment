#Number 1 .Print even numbers between 1 and 30
for x in range(1,30):
    while x % 2 == 0:
        print(x)
        x+=1

#Number 2. Print odd numbers between 1 and 30

for x in range(1,20):
    while x % 2 >=1:
        print(x)
        x+=1

#Number 3. Financial statement.

#Ahmed, an EiT Fellow, has been given an amount of GHC 50,000 for his capstone project.
#25% of this amount was spent on marketing, 
#50% was spent on other operational expenses, 
#The remaining 25% on customer acquisition, 
#It will cost him GHC 5 to acquire a customer
#Task: 
#Write a python program to prepare his financial statement
#Your program should calculate the number of customers he can acquire with the budget allocated

name = "Ahmed"
title = " EIT fellow"
doc = "Capstone Financial_Statement "
date = "22/10/2022"

print (doc + "\n" + name + ":" + title + "\n"  + "date:" + "" + date)
budget = 50000
marketing_percentage = 50/100
opEx_percentage = 0.25
customer_acquisition_percentage = 0.25

Marketing = budget * marketing_percentage
operationalExpenses = opEx_percentage  * budget
customer_acquisition = customer_acquisition_percentage * budget
cac = 5 
numberofcustomers = customer_acquisition / cac


print (f"Marketing budget --------------- {Marketing}" + "\n" + f"Operational Expenses(OpEx) -------{operationalExpenses}" + "\n"+
 f"Customer Acquisition Cost ------- {customer_acquisition}")
print(f"Total Number of customers acquired within the budget : {int(numberofcustomers)}")






