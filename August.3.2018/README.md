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

**Solution**: You have a **2/3** chance (0.6666667) to win the game.

I originally built a simulator for this game (which you can easily run for any number of trials and coin flips with the python file above), but I figured I should find the "elegant mathematical expression." 

If we flip the coin once, we have a 50% chance of winning the game. However, if we land tails then we will need to get two heads in a row. You have a 25% chance to land two heads in a row. So with three flips of the coin, we win the game 50% of the time by landing heads first, but in the 50% of games we land tails first we have an additional 25% of winning.

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?0.5%20&plus;%20%280.5%5Ccdot0.25%29%20%3D%200.625" alt="equation"/>
</p>

If we extend this to five coin flips we have a 50% chance of heads first, a 25% additional chance in the 50% times we flip tails first, plus another 12.5% chance if we flip two tails first (this would require three heads in a row, which happens 12.5% of the time).

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?0.5%20&plus;%20%280.5%5Ccdot%200.25%29%20&plus;%20%280.5%5Ccdot%200.5%5Ccdot%200.125%29%20%3D%200.65625" alt="equation"/>
</p>

At this point we can see a patter forming. Pulling the pieces apart we see...

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B2%5E%7Bn%7D%7D%5Ccdot%200.5%5E%7Bn-1%7D" alt="equation"/>
</p>

and with some reorganizing we get...

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?0.5%5Ccdot%200.25%5E%7Bn-1%7D" alt="equation"/>
</p>

This looks like a geometric series so we can use the basic geometric formula to find the answer.

<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?%5Csum_%7Bk%3D0%7D%5E%7Bn-1%7D%28ar%5E%7Bk%7D%29%3Da%28%5Cfrac%7B1-r%5E%7Bn%7D%7D%7B1-r%7D%29" alt="equation"/>
</p>
<p align="center">
  <img src="http://latex.codecogs.com/gif.latex?%5Csum_%7Bk%3D0%7D%5E%7Bn-1%7D%280.5%5Ccdot%200.25%5E%7Bk%7D%29%3D0.5%28%5Cfrac%7B1-0.25%5E%7Bn%7D%7D%7B1-0.25%7D%29%3D0.66666667" alt="equation"/>
</p>


