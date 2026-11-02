import random 
dice_roll = random.randint(1,6)
special_number = dice_roll == 1 or dice_roll == 6
print(f'dice roll number {dice_roll}')
print(f'special number {special_number}')