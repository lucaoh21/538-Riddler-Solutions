"""
Solution to the 538 Riddler Apil.6.2018 
Author: Luca Ostertag-Hill

To run the algorithm use transitiveChampions(), since parameters are defaulted,
or transitiveChampions(dataFilePath, 'Villanova').
"""

from pandas import DataFrame, read_csv
import pandas as pd, re      

"""
This is the main function for the NCAA Transitive Champions riddle. It uses a 
dictionary to keep track of each transitive champion (as the key) and a list of all
the games that made it a transitive champion (as the values). A list also had to be 
used, instead of recursion, because I wanted to find the shortest path to each
transitive champion. At the end, the function creates a txt file named 
'transitive-champions.txt' to store the list of champions and games that got them there.

Parameters: default parameters are already entered.
           - gameDataFilePath (csv file): File that contains all the NCAA season data.
           - champion (String): The NCAA champion.
"""
def transitiveChampions(gameDataFilePath=r'ncaa-games.csv', champion='Villanova'):
    
    data = pd.read_csv(gameDataFilePath)
    
    championDict = {champion: []}
    championList = [champion]
    for team in championList: 
        findUpsets(team, championDict, championList, data)
    
    finalDataFile = open(r'transitive-champions.txt', 'w')
    for key in championDict:
        finalDataFile.write(key + '\n')
        for game in championDict.get(key):
            finalDataFile.write(game + '\n')
        finalDataFile.write('\n')

"""
Function that checks if the transitive champion lost any games to any teams
who are not yet considered transitive champions. If a new champion is found, 
they are added to the overall list and dictionary.
"""
def findUpsets(team, championDict, championList, data):
    games = data.loc[(data['Team #2'] == team)]    

    for index, row in games.iterrows():
        score1 = row['Score #1']
        score2 = row['Score #2']        
        team2 = row['Team #1']            
        if team2 not in championDict:
            championList.append(team2)
            championDict[team2] = championDict.get(team) + [team2 + 
                " vs. " + team + ": " +  str(score1) + " to " + str(score2)]


########################################################################################
########################################################################################

"""
This function was used to parse the data from MasseyRatings into a 
csv file that could be properly used by pandas framework. Not required 
if you use the csv file included in this package. If you downloaded the
txt file to run this function use modifyDataFile('ncaa-games.txt', 'ncaa-games.csv'),
where the first parameter is the txt file and the second is an empty csv file
this function can write to. 
"""
def modifyDataFile(filePath, csvFilePath):
    readFile = file(filePath, 'r')
    
    csvFile = open(csvFilePath, "w")
    titleRow = "Team #1,Score #1,Team #2,Score #2\n"
    csvFile.write(titleRow)    

    pattern = re.compile(r'@?([\D+\s]+)\s+' r'(\d+)\s+' r'@?([\D+\s]+)\s+' r'(\d+)')
    for line in readFile:
        data = pattern.search(line)
        team1 = data.group(1).strip(' @')
        score1 = data.group(2)
        team2 = data.group(3).strip(' @')
        score2 = data.group(4)
        csvFile.write(team1 + ',' + score1 + ',' + team2 + ',' + score2 + '\n')
 
    readFile.close()