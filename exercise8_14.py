def average_price_per_year(dates,prices):
    year = ''
    counter = 0
    accumulator = 0
    average_year_years = []
    average_year_prices = []
    # for every date in the date list
    # do the following
    for index in range(len(dates)):
        # Set the first year.
        if year == '':
            year = dates[index][6:10]
            accumulator += float(prices[index])
            counter += 1
        # Continue with the rest dates.
            # if we are still in the same year then
        elif dates[index][6:10] == year:
                # add the price to the accumulator
                accumulator += float(prices[index])
                counter += 1
            # if the year changed, caclculate the average for the year
            # and continue with the next year.
        else:
            average = accumulator / counter
            average_year_years.append(year)
            average_year_prices.append(average)
            year = dates[index][6:10]
            counter = 0
            accumulator = 0
    print('Average Prices for Each Year')
    print('----------------------------')
    print()
    print('Year\t\tPrice')
    print('----\t\t-----')
    for index in range(len(average_year_years)):
        print(average_year_years[index],'\t--->\t',format(average_year_prices[index],',.2f'))


def average_price_per_month(dates,prices):
    month = ''
    year = ''
    counter = 0
    accumulator = 0
    average_price_months = []
    average_price_prices = []

    for index in range(len(dates)):
        if year == '':
            year = dates[index][6:10]
            if month == '':
                month = dates[index][0:2]
            elif dates[index][0:2] == month:
                accumulator += float(prices[index])
                counter += 1
            else:
                average = accumulator / counter
                average_price_months.append(

def highest_lowest_price_per_year():
    pass

def list_of_prices_lowest_to_highest():
    pass

def list_of_prices_highest_to_lowest():
    pass

def main():
    infile = open('GasPrices.txt', 'r')
    infile_list = infile.readlines()
    date_list = []
    price_list = []
    for line in infile_list:
        date_list.append(line[0:10])
        price_list.append(line[11:].rstrip('\n'))
    infile.close()
    average_price_per_year(date_list,price_list)


main()
