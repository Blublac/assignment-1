my_list = ["this",True, "student", 45, 66.43]
print(my_list)
c = my_list.copy()
print(c)

colors = ["Red","Green","White","Black", "Pink", "Yellow"]
del colors[0]
del colors[-1]
del colors[-1]
print(colors)


User_favourite_colour = input("enter your favourite colour\n>")
colors.append(User_favourite_colour)
print(colors)


list_1 = [10,20, [300, 400,[5000,6000],500],30,40 ]
list_1[2][2].append(7000)
print(list_1)
