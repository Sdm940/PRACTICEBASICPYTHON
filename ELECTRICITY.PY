a=int(input("Enter the number of units consumed: "))
p=int(input("Enter the price per unit: "))
total=a*p*1
print("Total electricity bill: ", total)
payment=int(input("Enter the amount you want to pay: "))
if payment>=total:
    change=payment-total
    print("Payment successful! Your change is: ", change)   
else:
    print("Insufficient payment. Please insert more money.")    
