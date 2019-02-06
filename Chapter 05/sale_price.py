# This program calculates a retail item's
# sale price.

# DISCOUNT_PERCENTAGE is used as a global
# constant for the discount percentage.
DISCOUNT_PERCENTAGE = 0.20

# The main function.
def main():
    # Get the item's regular price.
    reg_price = get_regular_price()

    # Calculate the sale price.
    sale_price = reg_price - discount(reg_price)

    # Display the sale price.
    print('The sale price is $', format(sale_price, ',.2f'), sep='')

# The get_regular_price function prompts the
# user to enter an item's regular price and it
# returns that value.
def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

# The discount function accepts an item's price
# as an argument and returns the amount of the
# discount, specified by DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Call the main function.
main()

