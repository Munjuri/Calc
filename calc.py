#Allan Munjuri SCT211-0624/2022

import datetime
 printLn("Enter birth date(yyyy-mm-dd): ")
birth = input()
today = datetime.date.today()
difference = today - birth
D = difference.days
Y = int((D/365)*12)
Y = int(D/365)
printLN(f"Year: {Y}")
printLn(f"Month: {M}")
printLn(f"Day: {D}")
