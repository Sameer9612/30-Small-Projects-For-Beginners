Weight = float(input("Enter Your Weight in kg: "))
Height = float(input("Enter Your Height in cm: "))

Height=Height/100 #it convert height in centimeter to meter

BMI = Weight/(Height*Height)

print("Your Body Mass Index is: ", BMI)

if BMI>0:
    if BMI<=18.5:
        print("You Are Underweight")
    
    elif BMI<=24.9:
        print("You Are Normal")
    
    elif BMI<=29.9:
        print("You Are Overweight")

    elif BMI<=34.9:
        print("You Are Obese")

    elif BMI>35:
        print("You Are Extremely Obese")

