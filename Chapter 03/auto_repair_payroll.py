# Variables to represent the base hours and
# the overtime multiplier.
base_hours = 40       # Base hours per week
ot_multiplier = 1.5   # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > base_hours:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - base_hours

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    # Calculate the gross pay.
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print('The gross pay is $', format(gross_pay, ',.2f'), sep='')


    
