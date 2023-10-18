name=input("please enter your name: ")
last_name=input("please enter your lastname: ")
sub1= float(input("enter youe first grade: "))
sub2=float(input("enter your second grade: "))
sub3=float(input("enter your third grade: "))
avr=(sub1+sub2+sub3)/3

if avr>17:
    print(name + last_name, ",you are Great!")

if 12<=avr<17:
    print(name + last_name, ",you are normal!")

if avr<12: 
    print(name + last_name, ",you have failed! ")
