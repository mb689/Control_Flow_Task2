Hours = int(input("What is hours for this week? "))
Pay = float(input("What is you pay rate? "))

if Hours > 40:
    Payment = 40 * Pay
    extraHours = Hours - 40
    newPay = 1.5 * Pay
    Payment += (newPay * extraHours)
    print(f"You done {Hours} hours and will be paid £{Payment}")
else:
    Payment = Hours * Pay
    print(f"You done {Hours} hours and will be paid £{Payment}")
