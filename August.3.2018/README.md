# The Eternal Question: How Much Do These Apricots Weigh?

>**Riddler Express:** A small fruity puzzle: you loaded a drying shed containing 1,000 kilograms of apricots. They were 99 percent water. After a day in the shed, they are now 98 percent water. How much do the apricots weigh now?

**Solution:** The apricots weigh **500kg**.

Originally the apricots weighed 1000kg and 99% was water weight. This means that 1% (or 10kg) of the apricots was another substance. After a day in the shed the apricots are only 98% water. Without thinking, a natural inclination might be to assume that 1% of water was lost so the apricots weigh 10kg (1%) less than the day before. However, this is incorrect. 

The apricots are now 98% water, which means that the other substance now comprises 2% of the apricots. The proportion of that substance doubled overnight from 1% to 2% yet the weight of the substance (10kg) was not altered. If 2% of the apricots weighs 10kg, then simple arithmetic (10kg * (100/2)) tells us that the apricots now weigh 500kg.

>**Riddler Classic:** I flip a coin. If it’s heads, I’ve won the game. If it’s tails, then I have to flip again, now needing to get two heads in a row to win. If, on my second toss, I get another tails instead of a heads, then I now need three heads in a row to win. If, instead, I get a heads on my second toss (having flipped a tails on the first toss) then I still need to get a second heads to have two heads in a row and win, but if my next toss is a tails (having thus tossed tails-heads-tails), I now need to flip three heads in a row to win, and so on. The more tails you’ve tossed, the more heads in a row you’ll need to win this game.
>
>I may flip a potentially infinite number of times, always needing to flip a series of N heads in a row to win, where N is T + 1 and T is the number of cumulative tails tossed. I win when I flip the required number of heads in a row.
>
>What are my chances of winning this game? (A computer program could calculate the probability to any degree of precision, but is there a more elegant mathematical expression for the probability of winning?)

**Solution**: You have a **0.7112119**% chance to win the game.

I originally built a simulator for this game (which you can easily run for any number of trials and coin flips with the python file above), but I figured I should try to find the "elegant mathematical expression." With 1,000,000 trials and a coin flip depth of 500 on my simulator I got a value of 0.71121190.

My line of thought was that if we flip the coin once, we have a 50% chance of winning the game. However, if we land tails then we will need to get two heads in a row. You have a 25% chance to land two heads in a row. So with three flips of the coin, we win the game 50% of the time by landing heads first, but in the 50% of games we land tails first we have an additional 25% of winning.

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?0.5%20&plus;%20%280.5%5Ccdot0.25%29%20%3D%200.625" alt="equation"/>
</p>

If we extend this to five coin flips we have a 50% chance of heads first, a 25% additional chance in the 50% times we flip tails first, plus another 12.5% chance if we flip two tails first (this would require three heads in a row, which happens 12.5% of the time).

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?0.5%20&plus;%20%280.5%5Ccdot%200.25%29%20&plus;%20%280.5%5Ccdot%200.5%5Ccdot%200.125%29%20%3D%200.65625" alt="equation"/>
</p>

At first I thought it would be as easy as finding the solution to the geometric series that appears to be forming. But through my simulator I realized my values were off, and that the number of possible solutions for the number of allowed coin flips grows in a very odd pattern. I noticed that with 1 coin flip there is 1 possibility to win. With 2 coin flips that number does not increase. I laid out more of these in the chart below.

| # Coin Flips | # Solutions|
-------------|---------------
1 | 1
2 | 1
3 | 2
4 | 2
5 | 3
6 | 4
7 | 5
8 | 7
9 | 10
10 | 14

I couldn't find a correlation in the growth of the solutions so I went back to the value my simulator produced. After searching online it turns out someone else was also looking for the mathematical expression for the value 0.71121190, and found that the equation uses the Q-Pochhammer symbol. After another quick search I found the expression I was looking for.

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?1%20-%20Q%5B%5Cfrac%7B1%7D%7B2%7D%5D%3D0.7112119" alt="equation"/>
</p>

Credit for this equation goes to [Reddit Math](https://www.reddit.com/r/math/comments/172jjw/how_can_one_determine_the_limit_of_the/).

