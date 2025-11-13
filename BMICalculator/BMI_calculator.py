def get_weight():
    while True:
        weight,weight_unit=input("Enter your weight").split()
        try:
            w=float(weight)
        except ValueError:
            print("Invalid weight! Please enter a valid integer")
            continue
        if  w<=0 or w>=700:
            print("Invalid weight")
            continue
        unit=weight_unit.lower()
        if unit=="kg":
            return w
        elif unit in ["pound","pounds","lb","lbs"]:
            return w*0.453592 
        else:
            print("Invalid unit! Enter the weight in kg or pounds!")


def get_height():
    while True:
        print("press 1 to enter height in metre")
        print("press 2 to enter height in foot and inches")
        try:
            choice=int(input())
        except ValueError:
            print("Enter the integer for choice")
            continue
        if choice==1:
            height=input("enter the height in metre")

            try:
                h=float(height)
            except ValueError:
                print("Invalid height! Please enter a proper number")
                continue

            if h<=0 or h>3:
                print("Invalid height")
                continue
            return h
        elif choice==2:
            foot=input("enter foot")
            inches=input("enter inches")
            try:
                f=int(foot)
                i=int(inches)
            except ValueError:
                print("Invalid height! please enter a proper number")
                continue
            h_in_metre=(f*12+i)*0.0254
            return h_in_metre
        else:
            print("invalid choice")
            continue
            



def Calculate_BMI (w:float,h:float):
    BMI=round(w/(h*h),2)
    print(f"Your BMI:{BMI}")
    if BMI<18.5:
        print("Underweight")
    elif BMI>=18.5 and BMI<=24.9:
        print("Normal Weight")
    elif BMI>=25 and BMI<=29.9:
        print("Overweight")
    elif BMI>=30:
        print("Obesity")



if __name__ == "__main__":
    weight=get_weight()
    height=get_height()
    Calculate_BMI(weight,height)







