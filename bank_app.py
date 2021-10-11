#this is the bank app modified
import random
import time
import ast
userdata = {}
transactionlog = {}
with open("bankappdatabase.txt","r") as file0:
    call = file0.read()
    called = ast.literal_eval(call)
    print(called)
def transact_update(amount, transmode,crdt,account_no,acctbal):
    trnsdetails = {"amount":amount,"trntype":transmode,"trn":crdt}
    transactionlog[account_no].append(trnsdetails)
    print(f"Dear {accountdetails.get('Account_name')} your transaction of {amount} was successful and your new account balance is {acctbal}")
    

print("Welcome to Univelcity Bank of Africa")
a = True
while a:
    init_page = input("Press 'L' to Login and 'S' to signup today\n>>>").lower()
    if init_page == "l":
        account_no = input("ENTER ACCOUNT NUMBER\n>>>")
        passwords = input("ENTER YOUR PASSWORD\n>>>")
        accountdetails = userdata.get(account_no)
        acctbal = float(accountdetails["balance"])
        benefactordetails = userdata.get(account_no)
        beneacctbal = float(benefactordetails["balance"])
        if accountdetails and passwords == accountdetails.get("password"):
            time.sleep(1)
            print("Login Successful")
            time.sleep(2)
            print(f"welcom back {accountdetails.get('Account_name')}, Account balance is {accountdetails.get('balance')}")
            login = True
            while login:
                activity = input("please select an option\n>>>1:deposit\n>>>2:withdrawal\n>>>3:3:transfer\n>>>4:account balance\n>>>5:account statement\n>>>0:logout\n>>>")
                if activity == "1":
                    amount = float(input("Enter amount"))
                    acctbal+=amount
                    transact_update(amount,"deposit","credit",account_no,acctbal)
                    with open("bankappdatabase.txt","a") as database1:
                        database1.write(f"{transactionlog}")
                elif activity == "2":
                    amount = float(input("ENTER AMOUNT"))
                    acctbal -= amount 
                    transact_update(amount,"withdrawal","debit",account_no,acctbal)
                    with open("bankappdatabase.txt","a") as database1:
                        database1.write(f"{transactionlog}")
                elif activity == "3":
                    amount = float(input("ENTER AMOUNT"))
                    benefactor = input("ENTER DESTINATION ACCOUNT")
                    Pin = input("Enter your 4 digit pin")
                    if not Pin == accountdetails.get("pin",False):
                        print("INVALID PIN")
                        continue
                    if amount>acctbal:
                        print("INSUFFICENT FUND")
                        continue
                    if benefactordetails and Pin == accountdetails.get("pin",False):
                            if amount < acctbal:
                                acctbal -= amount
                                beneacctbal+=amount
                                transact_update(amount,"transfer","debit",account_no,acctbal)
                            
                                transact_update(amount,"transfer","credit",benefactor,beneacctbal)
                                with open("bankappdatabase.txt","a") as database1:
                                    database1.write(f"{transactionlog}")
                elif activity =="4":
                    Pin= input("ENTER YOUR PIN ")
                    if not Pin == accountdetails.get("pin",False):
                        print("INVALID PIN")
                        continue
                    else:
                        print(acctbal)
                elif activity == "5":
                    Pin= input("ENTER YOUR PIN ")
                    if not Pin == accountdetails.get("pin",False):
                        print("INVALID PIN")
                        continue
                    else:
                        print(transactionlog[account_no])
                else:
                    activity=="0"
                    cin =input("You sure u want to logout? press 0 to confirm")
                    if not cin == "0":
                        continue
                    else:
                        break

            #print(called.keys())
                    



    elif init_page == "s":
        s = True
        while s:
            Account_name = input("ENTER YOUR NAME PLEASE\n>>>")
            Email =input("ENTER YOUR EMAIL ADDRESS\n>>>")
            passwords=input("ENTER A PASSWORWD\n>>>")
            con_password = input("CONFIRM PASSWORD\n>>>")
            if passwords != con_password:
                print("Password doesnot match")
                continue
            elif not passwords.isdigit():
                print("PLEASE ENTER AT LEAST 6 DIGITS ")
                continue
            elif passwords.isalpha():
                print("ONLY DIGITS")
                continue
            elif len(passwords) <6 or len(passwords) > 15:
                print("LENGTH MUST BE BTW 6 TO 16 DIGITS")
                continue
            Pin = input("ENTER A 4 DIGIT PIN\n")
            con_pin = input("CONFIRM PIN\n")
            if Pin != con_pin:
                print("Pin does not match")
                continue
            elif not Pin.isdigit():
                print("PLEASE ENTER AT LEAST 6 DIGITS")
                continue
            elif Pin.isalpha():
                print("ONLY DIGITS")
                continue
            elif len(Pin) != 4:
                print("LENGTH MUST BE ONLY 4 DIGITS")
            account_no = str(random.randint(3010000000, 3019999999))
            acct_bal = 0
            print(f"Dear Customer,\n\t Your account has successfully been created, your account name is {Account_name} and your account number is {account_no}.\n\tThanks for creating an account.")
            data = [("pin",Pin),("Account_name",Account_name),("account_no",account_no),("balance", acct_bal),("password",passwords)]
            userdata[account_no] = {}
            userdata[account_no].update(data)
            transactionlog[account_no] = []
            with open("bankappdatabase.txt","a") as database:
                database.write(f"{userdata}\n")
            print(userdata)
            break


