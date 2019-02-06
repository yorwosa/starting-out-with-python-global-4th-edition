# This program calculates a salesperson's pay
# at Make Your Own Music.
def main():
    # Get the amount of sales.
    sales = get_sales()

    # Get the amount of advanced pay.
    advanced_pay = get_advanced_pay()

    # Determine the commission rate.
    comm_rate = determine_comm_rate(sales)

    # Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    # Display the amount of pay.
    print('The pay is $', format(pay, ',.2f'), sep='')

    # Determine whether the pay is negative.
    if pay < 0:
        print('The salesperson must reimburse')
        print('the company.')

# The get_sales function gets a salesperson's
# monthly sales from the user and returns that value.
def get_sales():
    # Get the amount of monthly sales.
    monthly_sales = float(input('Enter the monthly sales: '))

    # Return the amount entered.
    return monthly_sales

# The get_advanced_pay function gets the amount of
# advanced pay given to the salesperson and returns
# that amount.
def get_advanced_pay():
    # Get the amount of advanced pay.
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced = float(input('Advanced pay: '))

    # Return the amount entered.
    return advanced

# The determine_comm_rate function accepts the
# amount of sales as an argument and returns the
# applicable commission rate.
def determine_comm_rate(sales):
    # Determine the commission rate.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Return the commission rate.
    return rate

# Call the main function
main()
