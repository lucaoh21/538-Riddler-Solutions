# Transitive National Champions

>**The Riddler:** On Monday, Villanova won the NCAA men’s basketball national title. But I recently overheard some boisterous Butler fans calling themselves the “transitive national champions,” because Butler beat Villanova earlier in the season. Of course, other teams also beat Butler during the season and their fans could therefore make exactly the same claim.
>
>How many transitive national champions were there this season? Or, maybe more descriptively, how many teams weren’t transitive national champions?
>
>(All of this season’s college basketball results are here. To get you started, Villanova lost to Butler, St. John’s, Providence and Creighton this season, all of whom can claim a transitive title. But remember, teams beat those teams, too.)

**Solution:** Of the 1,362 teams in the NCAA, **1,185** of them are transitive national champions.

We were given an unformatted set of data, wherein each row contained a date, team names, team scores, and other less important information. Instead of just parsing the file normally (because I wanted to mess around with the Pandas framework), I parsed the relevant data into a csv file. I then read this file into a dataframe and my algorithm proceeded from there to find all of the transitive national champions.

In the end I produced a dictionary with transitive champions as the keys and the list of games that got them there as the values. In order for people to find their own schools, or look at the data in a visually pleasing way, I moved the results into a text file that contains all of the champions and their path to victory in nice containers. I found that Bowdoin's basketball team had a path of 10 games to become national champs, thanks to beating Bates, who beat Alma, who beat Ohio Northern.... who beat Villanova. 

```
Bowdoin
Butler vs. Villanova: 101 to 93
Seton Hall vs. Butler: 90 to 87
Rutgers vs. Seton Hall: 71 to 65
Stony Brook vs. Rutgers: 75 to 73
Norfolk St vs. Stony Brook: 74 to 68
Lynchburg vs. Norfolk St: 83 to 80
Ohio Northern vs. Lynchburg: 84 to 64
Alma vs. Ohio Northern: 81 to 79
Bates vs. Alma: 86 to 80
Bowdoin vs. Bates: 70 to 63
```
