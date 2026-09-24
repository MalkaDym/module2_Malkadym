#Campus Cafe Project
#Malka Dym
#September 24,2026
#MCON141
#Description: A program that will offer menu options and calculate the total of all the items chosen to purchase, including tax and tip

#PSUDOCODE
#Customer will get menu options for coffee and muffin with the prices listed besides it

#The customer will choose how many of each item he would like to purchase

#When he inserts an amount the quantity is multiplied by the items value

#The customer will proceed to choose what percent tip he would like to give in addition to the total price of his items

#Since the customer inserts the percentage as an int, it must be converted to a decimal so 'tip' converts 't' into a decimal which can now be multiplied and added to the total

#The cutomer will then receive a recipt that calculated the subtotal of his purchase, how much he will be paying in tip and what additional percent he will be charged for taxes, followed by the complete total of his order

#'print_recipt' function is what prints the recipt for every order. It includes an 'if/else' statement so only items ordered are printed (for example if I did not order any muffins, instead of writing '0 x muffins = $0.00' it does not include 'muffins' on the recipt). I also used the 'or' function so it prints the remainder of the recipt: tax, tip and total calculations on every order.

#Finally once all calclations are printed it will say Thank you!

def menu_options():
  print("==Campus Cafe==")
  print("Coffee= $2.25")
  print("Muffin= $2.75")

menu_options()
'''Prints all menu options because I grouped them as a function'''

coffee = int(input("How many Coffees?"))
muffin = int(input("How many Muffins?"))
'''Asks the customer to insert amount of coffees/muffins he would like to purchase'''
coffees = float(2.25 * coffee)
muffins = float(2.75 * muffin)
'''converts number entered by customer into price of total items x item value'''
t= int(input("Enter tip percent [e.g. 0%, 5%, 10%] ").strip("%"))
'''customer chooses percent tip he would like to give'''
tip= float(t/100)
'''the number he entered is converted into a decimal to be multiplied and added to the subtotal'''
total=float(coffees+muffins)
tips=float(total*tip)
tiptotal=(total*tip)+total
'''calculates the tip by multiplying the total by the percentage, then adding that result to the total'''
taxes= total * 0.08875
'''calculates taxes by multiplying total by tax rate and adding to the total'''

'''below is the function that prints the recipt'''
def print_recipt():
    print("---Recipt---")
    if coffee > 0:
        print(f"{coffee} x Coffee @ $2.25=   ${coffees:.2f}")
    if muffin > 0:
        print(f"{muffin} x Coffee @ $2.25=   ${muffins:.2f}")
    if coffee > 0 or muffin > 0:
        print(f"Subtotal:   ${total:.2f}")
        print(f"Tax (8.875%):   ${taxes:.2f}")
        print(f"Tip({t})%:   ${tips:.2f}")
        print(f"TOTAL:   ${total+taxes+tiptotal:.2f}")
        print("Thank you!")
'''the if statement above helps the recipt only print purchased items and nothing extra'''
print_recipt()