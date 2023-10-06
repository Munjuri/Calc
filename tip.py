#Allan Munjuri SCT211-0624/2022

println("Welcome to tipping system: ")
println("Enter bill amount: ")
bill = float(iput())
println("Enter number of people splitting bill: ")
people = int(input())

print('''Choose tip as percentage of total bill\n 1. 10%\n 2. 12%\n 3. 15%\n Choose number''')

opt = input()
match opt:
    case "1":
      tip = bill*0.1
      payment = round((tip + bill)/people, 2)
      print(f"Each person should pay: Ksh.{payment}")
    case "2":
      tip = bill*0.12
      payment = round((tip + bill)/people, 2)
      print(f"Each person should pay: Ksh.{payment}")
    case "3":
      tip = bill*0.15
      payment = round((tip + bill)/people, 2)
      print(f"Each person should pay: Ksh.{payment}")
      
