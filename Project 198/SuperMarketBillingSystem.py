Total = 0

while True:
    Customer_name = input("Name : ")
    while True: 
        Quantity = input("Enter the quantity of item : ")
        Items = int(input("Enter the no. of items : "))
        Total = Quantity*Items
        Repeat = input("Do you want to repeat this process (Yes/No/YES/NO/yes/no)")
        if Repeat == "No" or Repeat == "NO" or Repeat == "no" :
            break

        print("_"*50)
        print("Name : ",Customer_name)
        print("Total Cost : ",Total)
        print()
        print("*****Thank You For Shopping With Us*****")
        print("_"*50)

        New_customer = input("Go to the next person (Yes/No/YES/NO/yes/no)")
        if New_customer == "No" or New_customer == "NO" or New_customer == "no":
            break
        
