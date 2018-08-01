# The Case Of The Smudged Secret Message

>**Riddler Classic:** Riddler Nation has been enlisted by the Pentagon to perform crucial (and arithmetical) intelligence gathering. Our mission: decode two equations. In each of them, every different letter stands for a different digit. But there is a minor problem in both equations.
>
>In the first equation, letters accidentally were smudged on their clandestine journey to a safe room within Riddler Headquarters and are now unreadable. (These are represented with dashes below.) But we know that all 10 digits, 0 through 9, appear in the equation.

```
    E X M R E E K
+   E H K R E K K
_________________
  - K - H - X - E
```

>What digits belong to what letters, and what are the dashes?
>
>In the second equation, our mathematical spies have said that one of the letters in the equation is wrong. But they can’t remember which one. Which is it?

```
    Y T B B E D M K D
+   Y H D B T Y Y D D
______________________
  E D Y T E R T P T Y
```

**Solution:**

_Problem 1:_ We know that each letter matches a specific digit and that all 10 digits must appear in the equation. This puzzle can be solved by logically narrowing down what possible digit each letter could match.

- Since all carryover bits can only be 1, the **left-most dash must be a 1**
- 2 * E must be greater than or equal to 9 to result in a carryover, so E > 4
- K + K = (1)E, so E must also be even (E is either 6 or 8)(K is either 3, 4, 8, or 9)
- If E = 6, then E + E + (1) = 12 or 13 and if E = 8 then E + E + (1) = 16 or 17
  - Because E + E + (1) = (1)K, the options for K are limited down to 3 or 4
- If E = 8, then K = 4
  - This causes a problem with E + E + (1) = (1)K since 8 + 8 + (1) = 16 or 17, but never 14 (E != 8, K != 4)
- If E = 6, then K = 3
  - This does not cause a problem since 6 + 6 + (1) = 12 or 13 (so **E = 6** and **K = 3**)

```
    6 X M R 6 6 3
+   6 H 3 R 6 3 3
_________________
  1 3 - H - X - 6
```

- 6 + 3 in the tens place equals 9 (**rightmost dash = 9**)
- 6 + 6 in the hundreds place equals 12 (**X = 2** and there is a carryover)

```
         (1)
    6 2 M R 6 6 3
+   6 H 3 R 6 3 3
_________________
  1 3 - H - 2 9 6
```

- At this point we are left with digits 4, 5, 7, 8
- We know that R + R + carrover must be odd, so R + R + 1 = 15 or 17 (R = 7 or 8)
- Since 6 + 6 != 13 we need a carryover from X + H + (1), so X + H + (1) must be greater than or equal to 10
  - X is 2, so H has to be either 7 or 8 for there to be a carryover
- At this point R = 7 or 8, H = 7 or 8, and the dash underneath R + R must be 5 or 7
  - If the dash was 7, it would leave only 8 for both R and H so the **dash = 5**
  - For the dash to be 5, R + R + (1) must be 15, so **R = 7**
  - Since R = 7 then **H = 8**
- This leaves us with (1) + M + 3 = 8 so **M = 4** and 2 + 8 (X + H) is 10 (so the **dash = 0**)

```
    6 2 4 7 6 6 3
+   6 8 3 7 6 3 3
_________________
  1 3 0 8 5 2 9 6
```

_Problem 2:_ We will solve this in a similar manner to Problem 1.

- Again since Y + Y + (1) produces a carryover E, Y must be > 4 and **E = 1**
- D + D = Y tells us that Y is even (Y = 6 or 8 and D = 3 or 4)
  - Similar to last time if Y = 8 then D = 4, which doesn't satisfy the equation Y + Y + (1) = (1)D
  - Thus **Y = 6** and **D = 3**

```
    6 T B B 1 3 M K 3
+   6 H 3 B T 6 6 3 3
______________________
  1 3 6 T 1 R T P T 6
```

- To satisfy B + B + (1) = (1)1, there must be a carryover and **B = 5**
  - 5 + 5 + 1 = 11 so there is also a carrover to 5 + 3 + (1) = T

```
       (1|1)
    6 T 5 5 1 3 M K 3
+   6 H 3 5 T 6 6 3 3
______________________
  1 3 6 T 1 R T P T 6
```

- 1 + 5 + 3 = T so **T = 9**
- T + H = (1)6 and since T = 9, **H = 7**

```
    6 9 5 5 1 3 M K 3
+   6 7 3 5 9 6 6 3 3
______________________
  1 3 6 9 1 R 9 P 9 6
```

- 1 + 9 = R so **R = 0**
- At this point we are left with 2, 4, 8 and we know one of the remaining letters (M, K, or P) must be wrong
- The only way for M + 6 + (1) = P is if there is no carryover and **M = 2** and **P = 8**
- This leaves us with letter K
  - K + 3 = 9 so K must actually be 6, however Y = 6 so **K = Y**
  
```
    6 9 5 5 1 3 2 6 3
+   6 7 3 5 9 6 6 3 3
______________________
  1 3 6 9 1 0 9 8 9 6
```
