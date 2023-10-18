username = "Madhu"
password = "Madhu123"
atm_pin=1111

c_name = input("Enter your name:")
c_password=str(input("Enter your password:"))
c_pin=int(input("Enter ATM Pin:"))

if c_name == username and c_password==password:
    if c_pin==atm_pin:
        print('''
            1.Deposit
            2.withdraw
            3.ministatement
            4.Pin change
            5.exit''')
        amount = 50000
        option = int(input("Select your option:"))
        if option == 1:
            dep=int(input("Enter the amount"))
            amount+=dep
            print("Total amount:", amount)
        elif option == 2:
            withdraw=int(input("Enter the amount:"))
            amount-=withdraw
            print("Total Amount:", amount)
        elif option == 3:
            print("=====ATM=====")
            print("Username:", username)
            print("Total amount:", amount)
            print("Thanks for Visiting")
            print("=======================")
        elif option ==4:
            print("Enter your Exisiting Pin:")
            exisiting_pin=int(input())

            if exisiting_pin == atm_pin:
                print("Enter new pin:")
                new_pin=int(input())
                print("Password changed successfully")
            else:
                print("Please enter your old exisiting pin")
                exisiting_pin=int(input())


        elif option == 5:
            exit()
    else:
        print("Please Enter the correct credentials")