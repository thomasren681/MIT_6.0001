"""
This is the solution for problem set 1 a for MIT 6.001
all the test point given is revealed correct
"""

# let the user do the input
annual_salary = int(input("please give us your annual salary:"))
portion_saved = float(input("please give us your planned portion of salary to save:"))
total_cost = int(input("please enter the price of your dream house:"))


#set some unchanged parameters
annually_interest_rate = 0.04
monthly_salary = annual_salary/12
current_saving = 0.0
portion_down_payment = 0.25
total_month = 0


#other parameters that need further calculation
down_payment = portion_down_payment*total_cost
monthly_saving = monthly_salary*portion_saved

#using an explicit loop to recursivly add the saving and month
while(current_saving<down_payment):
    monthly_interest_revenue = current_saving * annually_interest_rate / 12
    current_saving += monthly_saving + monthly_interest_revenue
    total_month += 1

print(total_month)
