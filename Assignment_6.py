#bank program
import time
import random

userdata= {}
x = True
while x:
    init_page = input("PRESS 'L' TO LOGIN OR 'S' TO SIGNUP\n>>>").lower()
    if init_page == "l" or init_page == "login":
        account_no = input("Enter your account number:\n")
        pin = input("Enter your pin\n>>>")
        time.sleep(2)
        if account_no in userdata.keys():
            access_pin = userdata.get(account_no)
            if access_pin == pin:
                time.sleep(2)
                print("Login Successful")
                if account_no in userdata[Account_name]:
                    time.sleep(2)
                    print(f"Account balance is {account_balance}")
                    loggedin = True
                    while loggedin:
                        activity = input(">>>Deposit\n>>>Withdrawal\n>>>Transfer\nlogout\n>>>").lower().title()
                        if activity == "Deposit":
                            #print(account_balance)
                            depostit =int(input("Enter amount"))
                            account_balance +=depostit
                            print (f"New balance is {account_balance}")
                            continue
                        elif activity == "Withdrawal":
                            #print(f"Account balance is {account_balance}")
                            withdrawal = int(input("Enter amount"))
                            if not withdrawal > account_balance:
                                account_balance-= withdrawal
                                print (f"New balance is {account_balance}")
                            else:
                                print("Insufficent fund")
                            continue
                        elif activity == "Transfer":
                            transfer_amount = int(input("Enter Amount\n>>>"))
                            receiver = input("Benefactor account number")
                            if receiver in userdata.keys() and transfer_amount < account_balance:
                                print(f"Transfer the sum of {transfer_amount} to {receiver}\n>>>Enter PIN to continue")
                                confirmation = input()
                                if confirmation == access_pin:
                                    print("Processing...")
                                    account_balance-=transfer_amount
                                    time.sleep(2)
                                    print("Verifying transaction...")
                                    time.sleep(2)
                                    print("Transaction Sucessful.✔✔✔")
                                    print (f"New balance is {account_balance}")
                                    continue
                                else:
                                    print("INVALID PIN")
                                    continue
                            else:
                                print("ACCOUNT NOT FOUND IN DATABASE")
                                continue
                        elif activity == "Logout":
                            break

                        else:
                            print("INVALID OPTION")
                            continue
            else:
                print("PLEASE ENTER A VALID ACCOUNT NUMBER AND PIN")
                continue
                            
                        
                            

    elif init_page =="s" or init_page == "signup":
        reg = input("OPEN AN ACCOUNT? PRESS 'Y'\n>>>").lower()
        if reg  == "y":
            Account_name = input("Enter your full name First name Middle name and Last name\n>>>").title()
            date_of_birth = input("Enter date of birth YYYY MM DD\n>>>")
            Email = input("Enter Email address\n>>>")
            pin = input("Enter your 4 digit pin\n>>>")
            account_no = str(random.randint(1000000000,9999999999))
            account_balance = 0
            print(f"Dear Customer,\n\t Your account has successfully been created, your account name is {Account_name} and your account number is {account_no}.\n\tThanks for creating an account.") 
            userdata[account_no]= pin
            userdata[Account_name]= account_no,account_balance,date_of_birth,Account_name
