# DICE PROGRAM
import random
User=input('Enter (Roll) To Roll Dice : ' ).lower()
Number=[1,2,3,4,5,6]
if(User=='roll'):
    print(random.choice(Number))
else:
    print('Invalid')