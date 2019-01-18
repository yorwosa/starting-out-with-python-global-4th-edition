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
    return master_list

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



def main():
    infile = open('pbnumbers.txt', 'r')
    
    # Read the file and create a list.
    contents = infile.readlines()
    
    # Strip the '\n' from the end of the elements
    for index in range(len(contents)):
        contents[index] = contents[index].rstrip('\n')
    master_list = unified_list(contents)
    numbersfound,timesfound = times_each_appears(master_list)
    
    top10common(timesfound,numbersfound)
    bottom10common(timesfound,numbersfound)
    infile.close()
main()
