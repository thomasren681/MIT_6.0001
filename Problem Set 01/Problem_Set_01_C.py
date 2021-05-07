"""
This is the solution for problem set 1 b for MIT 6.001
all the test point given is revealed correct
"""

def compute_currrent_saving(monthly_saving):
    total_month = 0
    current_saving = 0
    while(total_month<36):
        total_month += 1
        if (total_month)%6 == 0:
            monthly_saving *= (1+0.07)
        monthly_interest_revenue = current_saving * 0.04 / 12
        current_saving += monthly_saving + monthly_interest_revenue
    return current_saving




# let the user do the input
annual_salary = int(input("please give us your annual salary:"))
#portion_of_semi_annual_salary_raise = 0.07
total_cost = 250000


#set some unchanged parameters
#annually_interest_rate = 0.04
monthly_salary = annual_salary/12
current_saving = 0.0
portion_down_payment = 0.25
total_month = 0

#basic set for bisection search
low = 0.0
high = 1.0
portion_saved = 0
step_of_bisection_search = 0

#other parameters that need further calculation
down_payment = portion_down_payment*total_cost


#using an explicit loop to recursivly add the saving and month
while(abs(current_saving-total_cost)>100):
    portion_saved = (low + high)/2

    monthly_saving = monthly_salary * portion_saved

    current_saving = compute_currrent_saving(monthly_saving)

    if current_saving<total_cost:
        low = portion_saved
    else:
        high = portion_saved

    step_of_bisection_search +=1

    total_month = 0


print(low,high)
print("the total saving under this portion is :", current_saving)
print("best savings rate: %.4f" % portion_saved )
print("steps in bisection search: ", step_of_bisection_search)