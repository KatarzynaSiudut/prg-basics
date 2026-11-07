ean = input("enter ean: ")

if len(ean) == 13 and ean.isdigit():
    print("correct")

    if ean[0:3] == "590":
        print("in poland")

else:
    print("ean is incorrect")
