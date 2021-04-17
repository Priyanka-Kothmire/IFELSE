quantity=int(input("enter the value :"))
discount=0
if quantity>=1000:
    discount=discount+(quantity*10/100)   
    print("your value is to pay",quantity-discount)
else:
    print(quantity)





