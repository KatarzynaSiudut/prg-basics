age = float(input("enter your age:"))

if age < 13:
    print("your a child")
elif age >= 13 and age <= 19:
    print("your a teen")
elif age >= 20 and age <= 64:
    print("your an adult")
elif age >= 65:
    print("your a senior")