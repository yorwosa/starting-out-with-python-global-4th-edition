# Powerball Lottery

# 5 numbers 1-69
# 1 powerball number 1-26
##import random
##
##def lottery():
##    numbers = []
##    powerballs = []
##    for i in range(5):
##        number = (str(random.randint(1,69)))
##        if len(number) == 1:
##            number = '0' + number
##        numbers.append(number)
##    powerball = (str(random.randint(1,26)))
##    if len(powerball) == 1:
##        powerball = '0' + powerball
##    powerballs.append(powerball)
##    winning_numbers_list = numbers + powerballs
##    winning_numbers = ''
##    for number in winning_numbers_list:
##        winning_numbers += number + ' '
##    winning_numbers = winning_numbers.rstrip()
##    print(winning_numbers)
##    return winning_numbers
##
##def main():
##    outfile = open('pbnumbers.txt','w')
##    for i in range(1,655):
##        line = lottery()
##        print(line)
##        outfile.write(line + '\n')
##    outfile.close()
##main()



def unified_list(number_list):
    master_list = []
    for draw in number_list:
        draw_list = draw.split()
        master_list += draw_list
    return master_list, draw_list

def times_each_appears(a_list):
    counter = 0
    numbersfound = []
    timesfound = []
    
    # Iterate each number in the list.
    for number in a_list:
        if number not in numbersfound:
            # Setup a counter to check how many times a number is seen.
            counter = 0
        
            # Check how many times the number is in this list.
            for searchnumber in a_list:
            
                # If the number is found, add + 1 to the counter.
                if number == searchnumber:
                    counter += 1
       
        if number not in numbersfound:
            numbersfound.append(number)
            timesfound.append(counter)
    return numbersfound,timesfound
    
def top10common(times,numbers):
    counter = 0
    index = 0
    top10times= []
    top10numbers = []
    for count in range(10):
        # Find the index number of the number that appears the most times.
        index = (times.index(max(times)))
        # Add this number to the list top10numbers
        top10numbers.append(numbers[index])
        # Add the number of times it was found to top10times
        top10times.append(times[index])
        # remove the number from the searchlist
        del numbers[index]
        del times[index]
    print('Most Common Numbers')
    print('-------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(top10numbers)):
        print(top10numbers[index] + '\t--->\t' + str(top10times[index]))
    print()

def bottom10common(times,numbers):
    counter = 0
    index = 0
    bottom10times = []
    bottom10numbers = []
    for count in range(10):
        # Find the index of the number that appear the least times.
        index = times.index(min(times))
        # Add this number to the bottom10numbers
        bottom10numbers.append(numbers[index])
        # Add the number of times it was found to the bottom10times list
        bottom10times.append(times[index])
        # remove the number from the lists times and numbers.
        del numbers[index]
        del times[index]
    print('Least Common Numbers')
    print('--------------------')
    print('Numbers\t\tTimes')
    print('-------\t\t-----')
    for index in range(len(bottom10numbers)):
        print(bottom10numbers[index] + '\t--->\t' + str(bottom10times[index]))
    print()

def top10overdue(times,numbers,original_list):
    count = 0
    overdue_list = []
    not_seen_list = []
    placeholder = ''
    for number in numbers:
        placeholder = number
        for specific_number in numbers:
            if specific_number == placeholder:
                count = 0
            else:
                count += 1
        overdue_list.append(number)
        not_seen_list.append(count)
    top10overdue =[]
    top10notseenfor =[]
    for count in range(10):
        index = not_seen_list.index(max(not_seen_list))
        top10notseenfor.append(not_seen_list[index])
        top10overdue.append(overdue_list[index])
        del not_seen_list[index]
        del overdue_list[index]
    print("Overdue List")
    print("------------")
    print()
    print('Number\t\tOverdue')
    print('------\t\t-------')
    for index in range(len(top10overdue)):
        print(top10overdue[index] + '\t--->\t' + str(top10notseenfor[index]))
    print()

def seperate_frequency(a_list):
    powerballs = []
    powerballs_count = []
    non_powerballs = []
    non_powerballs_count = []
    counter = 0
    number = 0
    for count in range(1,27):
        number = count
        # Split the list into draws
        for draw in a_list:
            draw_list = draw.split()
            if int(draw_list[5]) == number:
                counter += 1
        powerballs.append(number)
        powerballs_count.append(counter)
        counter = 0

    for count in range(1,70):
        number = count
        for draw in a_list:
            draw_list = draw.split()
            for searchnumber in draw_list:
                if int(searchnumber) == number:
                    counter += 1
        non_powerballs.append(number)
        non_powerballs_count.append(counter)
        counter = 0
        
    print('Powerballs Frequency')
    print('--------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(powerballs)):
        print(str(powerballs[index]) + '\t--->\t' + str(powerballs_count[index]))
    print()
    print('Regulars Frequency')
    print('------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(non_powerballs)):
        print(str(non_powerballs[index]) + '\t--->\t' + str(non_powerballs_count[index]))

def main():
    infile = open('pbnumbers.txt', 'r')
    
    # Read the file and create a list.
    contents = infile.readlines()
    
    # Strip the '\n' from the end of the elements
    for index in range(len(contents)):
        contents[index] = contents[index].rstrip('\n')
    master_list,split_list = unified_list(contents)
    numbersfound,timesfound = times_each_appears(master_list)
    
    top10common(timesfound,numbersfound)
    bottom10common(timesfound,numbersfound)
    top10overdue(timesfound,numbersfound,master_list)
    seperate_frequency(contents)
    infile.close()
main()
