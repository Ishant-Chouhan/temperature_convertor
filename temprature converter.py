#temperature converter
print("enter 1 to  convert celcious into fernhite")
print("enter 2 to  convert fernhite into celcious")
def temperature_convertor():
    choice=input("enter your choice: ")
    if(choice=="1"):
        a=int(input("enter temperature in celcious: "))
        b=(a*(9/5))+32
        print(b,"Fernhite is equal to",a,"celcious")
    elif(choice=="2"):
        a=int(input("enter temperature in Frenhite: "))
        b=(a-32)*(5/9)
        print(b,"celcious is equal to",a,"Frenhite")
    
temperature_convertor()


    
