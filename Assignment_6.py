#bank program
import time
import random

transactions ={}
userdata= {'9769622562': {'pin': '1000', 'names': 'Lg', 'account_num': '9769622562', 'email': 't', 'DOB': 'g', 'balance': 0}, '9703314731': {'pin': '2000', 'names': 'W', 'account_num': '9703314731', 'email': 'f', 'DOB': 'er', 'balance': 0}}
userlog ={}
x = True
while x:
    init_page = input("PRESS 'L' TO LOGIN OR 'S' TO SIGNUP\n>>>").lower()
    if init_page == "l" or init_page == "login":
        account_no = input("Enter your account number:\n")
        pin = input("Enter your pin\n>>>")
        time.sleep(2)
        account_details = userdata.get(account_no,False)
        if account_details and pin == account_details.get("pin") :
            print("Login Successful")
            time.sleep(2)
            print(f"Account balance is {account_balance}")
            credit = []
            debit = []
            loggedin = True
            while loggedin:
                activity = input(">>>D: Deposit\n>>>W: Withdrawal\n>>>T: Transfer\n>>>C: Check your balance\n>>>S: Account statement\n>>>L: Logout\n>>>").title()
                if activity == "D":
                    #print(account_balance)
                    deposit =int(input("Enter amount"))
                    account_balance +=deposit
                    print (f"New balance is {account_balance}")
                    credit.append(f"${deposit}")
                    credit.reverse()
                    print(credit)
                    continue
                elif activity == "W":
                    #print(f"Account balance is {account_balance}")
                    withdrawal = int(input("Enter amount"))
                    if not withdrawal > account_balance:
                        account_balance-= withdrawal
                        print (f"New balance is {account_balance}")
                        debit.append(f"Wd ${withdrawal}")
                        debit.reverse()
                        print(debit)
                    else:
                        print("Insufficent fund")
                    continue
                elif activity == "T":
                    transfer_amount = int(input("Enter Amount\n>>>"))
                    receiver = input("Benefactor account number")
                    if receiver in userdata.keys() and transfer_amount < account_balance:
                        print(f"Transfer the sum of {transfer_amount} to {receiver}\n>>>Enter PIN to continue")
                        confirmation = input()
                        if confirmation == userdata[account_no].get("pin",False):
                            print("Proces sing...")
                            account_balance-=transfer_amount
                            time.sleep(2)
                            print("Verifying transaction...")
                            time.sleep(2)
                            print("Transaction Sucessful.✔✔✔")
                            print (f"New balance is {account_balance}")
                            debit.append(f"Trf ${transfer_amount}")
                            debit.reverse()
                            print(debit)
                            continue
                        else:
                            print("INVALID PIN")
                            continue
                    else:
                        print("ACCOUNT NOT FOUND IN DATABASE")
                        continue
                elif activity =="C":
                    print(f"Your account balance is ${account_balance}")
                elif activity == "S":
                    statement  = input("Enter your account number")
                    if statement == userdata.get(account_no,False):
                        transactions = credit,debit
                        userlog[account_no] = transactions
                        print(userlog)

                elif activity == "L":
                    break

                else:
                    print("INVALID OPTION")
                    continue
            else:
                print("PLEASE ENTER A VALID ACCOUNT NUMBER AND PIN")
                continue
                            
                        
                            

    elif init_page =="s" or init_page == "signup":
        signup = True
        while signup:
            reg = input("OPEN AN ACCOUNT? PRESS 'Y'\n>>>").lower()
            if reg  == "y":
                Account_name = input("Enter your full name First name Middle name and Last name\n>>>").title()
                date_of_birth = input("Enter date of birth YYYY MM DD\n>>>")
                Email = input("Enter Email address\n>>>")
                password = input("Create a password")
                confirm_pass = input("Confirm password")
                if password != confirm_pass:
                    print("Password does not match")
                    continue
                elif len(password) > 16 or len(password) < 6:
                    print("Password must be between 6-1610000 characters")
                    continue
                pin = input("Enter your 4 digit pin\n>>>")
                if len(pin) > 4 or len(pin) < 4: 
                    print ("PIN must be four digits")
                    continue
                elif not pin.isdigit():
                    print("ONLY NUMBERS ALLOWED")
                    continue
                else:
                    pass
                account_no = str(random.randint(9000000000,9999999999))
                account_balance = 0
                print(f"Dear Customer,\n\t Your account has successfully been created, your account name is {Account_name} and your account number is {account_no}.\n\tThanks for creating an account.") 
                data = [("pin",pin),("names", Account_name ),("account_num", account_no),("email", Email),("DOB",date_of_birth),("balance",account_balance)]
                userdata[account_no] = {}
                userdata[account_no].update (data)
                print(userdata)
            signup = False