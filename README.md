# repeatingDivisions

Simple python3 script for conversion between (possibly repeating) decimal representations of fractions and fractions. It has two uses:

1. It can be used to calculate a division between integers (it doesn't currently work for negative integers, but it should be pretty easy to work around that), producing a string of the form

      **integer-part** . **decimal-part** ( **repetend** )
      
      Note that in cases such as 1 / 1, where both 1.(0) and 0.(9) are legit, it will always prefer the "terminating" one, that is 1.(0)
  
2. It can also be used to do the opposite thing, a.k.a. produce the lowest form fraction that produces that decimal representation. 

DISCLAIMER: As of now, I'm not supporting this thing, but I *might* if someone shows interest in it. Anyway, I strongly doubt it'll happen: this code is really simple and should be fairly easy to reproduce for anyone who as any experience in programming.
