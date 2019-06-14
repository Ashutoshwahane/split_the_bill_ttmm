from time import *
print("**********-------------------------------***************")
sleep(0.25)
print("****===>>>  WELCOME TO THE SPLIT__BILL SYSTEM  <<<===****")
sleep(0.25)
print("Developed by *** Willskhalifa ***")
sleep(0.25)
print("**********-------------------------------***************")
sleep(0.25)
Total_Amount_bill = int(input("Enter the total amount of bill ==>> "))
people = []                                             #storing names  in people
paid_people = []                                        #storing paid amount according people
no_of_people = int(input("Enter the number of people ==>> "))
class Split:

    def take(self):
        for i in range(no_of_people):                      #getting the names
            name = input("Enter the Names ==>> ")
            people.append(name)
            rs = int(input("--how much he  paid -->"))     #getting the amount
            paid_people.append(rs)
    def show(self):
        div_amount = Total_Amount_bill / no_of_people       #dividing the amount
        print("**********-------------------------------***************")
        print()
        print(" per/person charge amount  ==> ", div_amount)
        print()
        print("**********-------------------------------***************")
        print()
        for i in range(no_of_people):                       #displaying the data
            print(people[i], " amount paid = ", paid_people[i])
            print()
        for i in range(no_of_people):
            if div_amount - paid_people[i] < 0:             #displaying the final data
                print("**********-------------------------------***************")
                print()
                print(people[i], " will get ",paid_people[i] - div_amount)
                print()
                sleep(0.25)
            else:
                print("**********-------------------------------***************")
                print()
                print(people[i], " needs to pay this amount ",div_amount - paid_people[i])
                print()
                sleep(0.25)
s = Split()
s.take()
s.show()
