#7. World Series Winners
#In this chapter’s source code folder (available on the Premium Companion Website at www.
#pearsonglobaleditions.com/gaddis), you will find a text file named WorldSeriesWinners.
#txt . This file contains a chronological list of the World Series’ winning teams from 1903
#through 2009. The first line in the file is the name of the team that won in 1903, and the
#last line is the name of the team that won in 2009. (Note the World Series was not played
#in 1904 or 1994. There are entries in the file indicating this.)
#Write a program that reads this file and creates a dictionary in which the keys are the names
#of the teams, and each key’s associated value is the number of times the team has won the
#World Series. The program should also create a dictionary in which the keys are the years,
#and each key’s associated value is the name of the team that won that year.
#The program should prompt the user for a year in the range of 1903 through 2009. It
#should then display the name of the team that won the World Series that year, and the
#number of times that team has won the World Series.

def readfile():
    infile = open('WorldSeries.txt','r')
    timeswon = dict()
    teamwon = dict()
    year = 1903
    team = infile.readline()
    dontskip = True
    while team != '':
        team = team.rstrip('\n')
        if team in timeswon:
            timeswon[team] += 1
        elif team.startswith('World'):
            dontskip = False
        else:
            timeswon[team] = 1
        if dontskip:
            teamwon[year] = team
        year += 1
        team = infile.readline()
        dontskip = True
    return teamwon,timeswon
def main():
    teamwon, timeswon = readfile()
    selection = int(input('Choose a year between 1903 and 2009: '))
    while selection == 1904 or selection == 1994:
        print('There was no world cup in',selection)
        selection = int(input('Choose another year:'))
    print(teamwon[selection],'won the World Cup in',selection)
    print('In total they won,',timeswon[teamwon[selection]],'times.')
main()