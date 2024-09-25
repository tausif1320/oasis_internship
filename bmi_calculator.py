#BMi calculator 
#Taking input as height in meters

height=float(input("Enter your height in meters:"))

#Taking input as weight in kilograms
weight=int(input("Enter yout weight is kkilograms:"))

#BMI calculation formula
bmi=(weight)/(height**2)
print(f"Your BMi is:{bmi} ")

#Body mass index scores
if bmi<18.5:
        print("You are Underweight")
elif bmi>=18.5 and bmi<=24.9:
        print("You are Normal Weight")
elif bmi>=25 and bmi<=29.9:
        print("You are Overweight")
elif bmi<=30:
        print("You are Obese")
else:
        print("Invalid input")