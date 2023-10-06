#Allan Munjuri SCT211-0624/2022

printIn("Enter your weight: ")
weight = float(input())
printLn("Enter your height: ")
height = float(input())/100
bmi = round(weight/(height**2), 1)
if bmi < 18.5:
  print(f"Your bmi is: {bmi}\n You are : underweight")

elif bmi >= 18.5 and bmi < 25.0:
  print(f"Your bmi is: {bmi}\n You are : normal weight")

else:
  print(f"Your bmi is: {bmi}\n You are : Overweight")
  
