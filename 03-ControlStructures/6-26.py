real_code = "0805"
attempts = 0
while attempts < 3:
    pin = input("enter the code: ")
    if pin == real_code:
        print("correct pin")
        break
    else:
        print("incorrect")
        attempts = attempts + 1 

if attempts == 3:
    print("sorry, your card is blocked")

