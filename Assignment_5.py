#build a password validate
user_FN = input("Plese enter your First name\n>>>> ")
user_LN = input("Please enter your Last name\n>>>> ")
userID = user_FN[:3] + user_LN[:-3]
print(userID)

symbols = ["#",",",".","?","&","*","@"]

max_length = 16
min_length = 6
password =input("PASSWORD PLEASE\n>>>> ")

if not password.upper().isalpha and  not password.lower().isalpha:
     print("Password must contain atleast 1 uppercase and 1 lowercase letter")
if not password.isdigit:
    print("Password must contain a number")
if  password != any in symbols:
    print("Password must contain a special character")
elif len(password) < min_length:
    print("Password too short")
elif len(password) > max_length:
    print("Password can't be more than 16 characters")
else:
    print("Password is perfect")
print(f"Dear {userID}, Your account is set and your password is {password}.Please do not share this password with anyone")


#program to check for triangle
side_a = input("Length of side a\n>>>>")
side_b = input("Length of side b\n>>>>")
side_c = input("Length of side c\n>>>>")
if side_a == side_b and side_a == side_c:
    print("THE TRIANGLE IS AN EQUILATERAL")
if side_a == side_b or side_a == side_c:
    print("THE TRIANGLE IS AN ISOSCELES")
if side_a != side_b and side_a != side_c:
    print("THE TRIANGLE IS A SCALENE")


#SORTING A LIST OF DICTIONARY
List_of_dictionary = [{"make":"nokia","model":216,"colour":"black"},{"make":"mi max","model":2,"colour":"gold"},{"make":"samsung","model":7,"colour":"blue"}]
sorted_list = sorted(List_of_dictionary,key=lambda x:x["colour"])
print(sorted_list)