import time
def start():
    #input number
    num1= input("Enter a number : ")
    num2= input("Enter another number : ")

    #select operator


    opselect= input ("What function do you want to add: \nA) Addition. \nB) Subtraction. \nC) Division. \nD) Multiplication. : \n")

    #if operator is selected, a calculation will happen

    #Addition
    if opselect== "A":
        result =float (num1)+float (num2)

    #Subtraction
    elif opselect== "B":
         result =float (num1)-float (num2)

    #Division
    elif opselect== "C":
         result =float (num1)/float (num2)

         #Multiplication
    elif opselect== "D":
         result =float (num1)*float (num2)

    print(result)

    repeat = input ("Do you wish to continue ? \nyes[] \nNo[]\n")
    if repeat==  "yes":
        print ("Hold on")
        time.sleep (1)
        start()

    else:
            print ("Bye")
            print ("Thank you for using this digital calculator :)")
            exit ()
start()
