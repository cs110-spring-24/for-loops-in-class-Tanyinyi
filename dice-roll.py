#Let’s simulate roll 100 dice and print out each dice value
import random
dice_1=0
dice_2=0
dice_3=0
dice_4=0
dice_5=0
dice_6=0
for roll in range(100):
    dice=random.randint(1,6)
    if dice==1:
        print("1")
        dice_1+=1
    elif dice==2:
        print("2")
        dice_2+=1
    elif dice==3:
        print("3")
        dice_3+=1
    elif dice==4:
        print("4")
        dice_4+=1
    elif dice==5:
        print("5")
        dice_5+=1
    elif dice==6:
        print("6")
        dice_6+=1
print(f"you rolled {dice_1} 1s,{dice_2} 2s, {dice_3} 3s, {dice_4} 4s, {dice_5} 5s, {dice_6} 6s")


    
