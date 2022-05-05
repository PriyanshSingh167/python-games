print("Welcome to the tip calculator.")

bill =float(input("What was the total bill? $"))

tip = input("How much tip would you like to give? 10, 12, or 15?")

totalBill = round((bill) * (1+int(tip)/100) , 2)

split = input("How many people to split the bill?")

finalBill = totalBill/int(split)

print(finalBill)