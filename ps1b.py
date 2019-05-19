#!/usr/bin/python3.6


######################################################################

#  	Total Months to Save Up for Down Payment

# 	Problem Set2 Test 2

######################################################################

annual_salary=int(input("Enter Annual Salary:"))

portion_saved=(float(input("Enter Portion of Salary to Be Saved")))

semi_annual_raise=float(input("Enter Semi Annual Raise"))
total_cost=int(input("Enter Total cost of Home:"))

portion_down_payment=total_cost*0.25

current_savings=0
months=1
while int(current_savings)<=portion_down_payment:
	if months%6==0:
		annual_salary+=annual_salary*semi_annual_raise
	current_savings+=(annual_salary/12)*portion_saved
	current_savings+=(current_savings*0.04)/12
	months+=1

print("Total No of Months:",months)


