No_of_students_who_subscried_to_English = input("How many students want English\n>")
list_of_No_of_students_who_reads_English = input("Enter English students list\n>")
No_of_students_who_subscribed_to_French = input("How many students want French\n>")
list_of_No_of_students_who_reads_French = input("Enter French students list\n")

a = set(list_of_No_of_students_who_reads_English.split())
b = set(list_of_No_of_students_who_reads_French.split())
subscribers = a.intersection(b)
print(subscribers)
print(len(subscribers))