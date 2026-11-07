dog_age = float(input('enter the dog years in human years:'))

if dog_age <= 2:
    dog_age_human = dog_age * 10.5
elif dog_age > 2:
    dog_age_human = 21 + (dog_age - 2)* 4

print(f'the dogs age in dogs years is: {dog_age_human}')