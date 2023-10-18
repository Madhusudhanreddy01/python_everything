from itertools import count
import csv


class Bank():
    def __init__(self) -> None:
        self.data = []
        self.field = ["Account Number","First Name","Middle Name","Last Name","Father Name","Address","Area","Pincode","State","Phone Number","Gmail","Date Of Borth","Amount"]
        
    def input_pincode(self):
        pin = int(input("Enter Pincode : "))
        if len(str(pin)) != 6:
            print("Invalid Input. Enter valid PIN Code")
            self.input_pincode()
        return pin

    def new_Account_Create(self):
        self.first_name = input("First Name : ")
        self.middle_name = input("Middle Name : ")
        self.last_name = input("Last Name : ")
        self.father_Name = input("Father Name : ")
        self.address = input("Address :")
        self.area = input("Area (or) Locality : ")
        self.pincode = self.input_pincode()
        self.state = input("State : ")
        self.phonenumber = input("Phone Number : ")
        self.gmailaddress = input("Gmail Address : ")
        self.dob = input("Date Of Birth : ")
        self.Amount = 0

        customer_names.append(self.first_name)
        len_customer_names = str(len(customer_names))
        if (len(len_customer_names) >0) and (len(len_customer_names) < 4):
            if len(len_customer_names) == 1:
                lastdigit = "00" + len_customer_names
                account_number = "1000000" + lastdigit
            if len(len_customer_names) == 2:
                lastdigit = "0" + len_customer_names
                account_number = "1000000" + lastdigit
            if len(len_customer_names) == 3:
                lastdigit = len_customer_names
                account_number = "1000000" + lastdigit
        self.account_number = account_number

        print("1.savings Account \n 2.Current Account \n 3.Fixed Deposit")
        
        
        type_acc = int(input("Please Select Your Account Type : "))
        if type_acc == 1:
            acc1 = "Savings Account"
        elif type_acc == 2:
            acc1 = "Current Account"
        elif type_acc == 3:
            acc1 = "Fixed Deposit"

        dic = {}
        customer_details = [self.account_number,self.first_name,self.middle_name,self.last_name,self.father_Name,self.address,self.area,self.pincode,self.state,self.phonenumber,self.gmailaddress,self.dob,self.Amount]

        for i in range(len(customer_details)):
            dic[self.field[i]] = customer_details[i]
        
        self.data.append(dic)

        self.write_csv(self.data, field=self.field)


    def write_csv(self, d, field):
        with open("data.csv", 'w') as cfile:
            writer = csv.DictWriter(cfile, fieldnames=field)
            writer.writeheader()
            writer.writerows(d)


    def existing_customer(user_list):
        account_details = input("Please Enter Your Account Number : ")
        count=0
        for i,j in user_Details.items():
            if account_details == i:
                count += 1
                print(user_Details[account_details])
                
        if count == 0:
            print("Your Enter Wrong Account Number , Please check Your Account Number")

        
    def deposite(self):
        cash = input("Please enter your AccountNumber = ")
        deposited = int(input("Please enter deposit amount  = "))
        count = 0
        for i,j in user_Details.items():
            if cash == i:
                count += 1
                k = (user_Details[cash]["Amount"])
                user_Details[cash].update({"Amount":k+deposited})
                boss = user_Details[cash]["Amount"]
        print(boss)
        if count == 0:

            print("Your Enter Wrong Please check The Account Number")

    def withdraw(self):
        cash = input("Please enter your AccountNumber = ")
        withdraw = int(input("Please enter withdraw amount  = "))
        count = 0
        for i,j in user_Details.items():
            if cash == i:
                count += 1
                k = (user_Details[cash]["Amount"])
                if k >=withdraw:
                    user_Details[cash].update({"Amount":k-withdraw})
                    boss = user_Details[cash]["Amount"]
                    
                else:
                    print("Sorry Insufficient Balance")
                print(boss)
        if count == 0:

            print("Your Enter Wrong Please check The Account Number")


customer_names=[]
customer_details=[]
user_Details={}
def main():
    b=Bank()
    n = 1
    while n > 0:
        print("Welcome To Your Bank")
        print("Choose Your Options To Continue")
        print("1.Create Your Account")
        print("2.Existing Account")
        print("3.Deposite Cash")
        print("4.Withdraw Cash")
        print("8.Quit")

        user = int(input("Please Select Your Choice  =  "))
        if user == 1:
            b.new_Account_Create()
        elif user ==2:
            b.existing_customer()
        elif user == 3:
            b.deposite()
        elif user == 4:
            b.withdraw()
        elif user ==8:
            break



if __name__ == '__main__':
    main()



