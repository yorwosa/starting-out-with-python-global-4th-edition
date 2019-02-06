# This program displays step-by-step instructions
# for disassembling an Acme dryer.
# The main function performs the program's main logic.
def main():
    # Display the start-up message.
    startup_message()
    input('Press Enter to see Step 1.')
    # Display step 1.
    step1()
    input('Press Enter to see Step 2.')
    # Display step 2.
    step2()
    input('Press Enter to see Step 3.')
    # Display step 3.
    step3()
    input('Press Enter to see Step 4.')
    # Display step 4.
    step4()

# The startup_message function displays the
# program's initial message on the screen.
def startup_message():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer.')
    print('There are 4 steps in the process.')
    print()

# The step1 function displays the instructions
# for step 1.
def step1():
    print('Step 1: Unplug the dryer and')
    print('move it away from the wall.')
    print()

# The step2 function displays the instructions
# for step 2.
def step2():
    print('Step 2: Remove the six screws')
    print('from the back of the dryer.')
    print()

# The step3 function displays the instructions
# for step 3.
def step3():
    print('Step 3: Remove the back panel')
    print('from the dryer.')
    print()

# The step4 function displays the instructions
# for step 4.
def step4():
    print('Step 4: Pull the top of the')
    print('dryer straight up.')

# Call the main function to begin the program.
main()
