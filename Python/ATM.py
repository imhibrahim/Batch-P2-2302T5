pincode="1234";
balance=5000;


print("----Welcome To Our ATM----");

userpin=input("Enter Your Pin Code 4 digits");

if userpin==pincode:
    while True:
        print("1: Check The Balence")
        print("2: Cash WithDraw")
        print("3: Cash Deposit")
        print("4: Exit")
        choice=input("Please Select Any Number :- ")

        if choice=="1":
            print("Your Balance Is :",balance)
        elif choice=="2":
            cash=float(input("Enter Your Cash"))
            if cash<=balance:
             balance-=cash
             print("Transection Seccessfully... \n Your Balance Is :",balance)
            else:
                print("Inceficent Balence")

        elif choice=="3":
            usercash=float(input('Enter Your Deposit Amount :- '))
            balance += usercash
            print("Deposit Seccessfully... \n Your Balance Is :",balance)

        elif choice=="4":
            print("thanks For Using For ATM")
            break

        else:
            print("Invalid Number")

else:
    print("Invalid Pin code.....")