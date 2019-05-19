#!/usr/bin/python3.6


######################################################################

#  	Total Months to Save Up for Down Payment

# 	Problem Set2 Test 1
######################################################################

annual_salary=int(input("Enter Annual Salary:"))

portion_saved=(float(input("Enter Portion of Salary to Be Saved")))/100

total_cost=int(input("Enter Total cost of Home:"))

portion_down_payment=total_cost*0.25

current_savings=0
months=1
while int(current_savings)<=portion_down_payment:
	current_savings+=(annual_salary/12)*portion_saved
	current_savings+=(current_savings*0.04)/12
	#print(int(current_savings)):::DEBUG
	months+=1

print("Total No of Months:",months)


