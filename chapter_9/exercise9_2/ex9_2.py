# Capital Quiz
def dictStatesCapitals():
    StatesCapitals = dict()
    cap_list = []
    stat_list = []
    infile = open('StatesCapitals.txt', 'r')
    StCap_list = infile.readlines()
    for capital in StCap_list[::2]:
        cap_list.append(capital.rstrip('\n'))
    for index in range(len(cap_list)):
        cap_list[index] = cap_list[index].rstrip()
    for state in StCap_list[1::2]:
        stat_list.append(state.rstrip('\n'))
    for index in range(len(stat_list)):
        stat_list[index] = stat_list[index].rstrip()
    for index in range(len(cap_list)):
        StatesCapitals[stat_list[index]] = cap_list[index]
    infile.close()
    return StatesCapitals

def main():
    import random
    questions = dictStatesCapitals()
    correct = 0
    wrong = 0
    print('Welcome to Capital Quiz')
    print()
    print('Do you know all the State Capitals?')
    print()
    for count in range(len(questions)):
        state, capital = questions.popitem()
        print('What is the capital of',state,'?: ',end = '')
        answer = input()
        if answer.lower() == capital.lower():
            correct += 1
            print('Correct')
            print('Next Question')
            print()
        else:
            wrong += 1
            print('Wrong')
            print('Next Question')
            print()
    print('Correct:',correct)
    print('Wrong:',wrong)
main()
