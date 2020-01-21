# This is a dictionary with items on a restaurants menu
# It will print out a receipt for each table's order
menu = {
    "Brunch" : {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": 8.99,
        "Egg Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad" : 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99,
        "Coffee": 1.99,
        "Orange Juice": 0.99,
        "Milk": 0.55,
        "Water": 0.00
    }
}

menu["Brunch"]["Steak Salad"] = 15.99
menu["Specials"] = {
    'Soup of the day' : 8.99,
    'Catch of the day' : 14.99,
    'Chef Special' : 15.99
    }
menu['Brunch']['Three Egg Breakfast'] = {
    'With Bacon': 8.99,
    'Without Bacon': 9.99 
    }

#Table 1
print("Bill for Table 1")
guest1_food = menu["Brunch"]['Egg Benedict']
guest2_food = menu['Brunch']['Biscuit and Gravy']
guest3_food = menu["Brunch"]["Steak and Eggs"]
guest1_drink = menu["Drinks"]["Coffee"]
guest2_drink = menu["Drinks"]["Coffee"]
guest3_drink = menu["Drinks"]["Soft Drink"]


print(" Egg Benedict: \t\t\t $ " + str(guest1_food )+ "\n Biscuit and Gravy: \t\t $ " + 
str(guest2_food) + "\n Steak and Eggs: \t\t $ " + str(guest3_food) + "\n Coffee: \t\t\t $ " + 
str(guest1_drink) + "\n Coffee: \t\t\t $ "+ str(guest2_drink) + "\n Soft Drink: \t\t\t $ " + str(guest3_drink))

table1_price = float(guest1_food + guest2_food + guest3_food + guest1_drink + guest2_drink + guest3_drink)
tax_1= table1_price * 0.07
total_1 = table1_price + tax_1

tip1 = total_1 * .25
tip2 = total_1 * .2
tip3 = total_1 * .15
price_print = print("\t\tPrice: $ " + format(table1_price, '.2f'))
tax_print = print("\t\tTaxes: $ " + format(tax_1,'.2f'))
total_print = print("\t\tTotal: $ " + format(total_1, '.2f')) 
print("**Suggested Tip** \nTip 25%: " + format(tip1, '.2f') + 
"\nTip 20%: " + format(tip2, '.2f') + "\nTip 15%: " + format(tip3, '.2f'))

# Table 2

print("\n\nBill for Table 2")
guest1_food_2 = menu["Brunch"]["Steak Salad"]
guest2_food_2 = menu["Specials"]['Soup of the day']
guest2_food2_2 = menu["Brunch"]["Chicken Wrap"]
guest3_food_2 = menu["Brunch"]["Chicken Fingers"]
guest1_drink_2 = menu["Drinks"]["Soft Drink"]
guest2_drink_2 = menu["Drinks"]["Water"]
guest3_drink_2 = menu["Drinks"]["Soft Drink"]
table = menu["Specials"]["Chef Special"]

print(" Steak Salad: \t\t $ " + str(guest1_food_2 )+ "\n Soup of the day: \t $ " + 
str(guest2_food_2) + "\n Chicken Wrap \t\t $ " + str(guest2_food2_2) + 
"\n Chicken Fingers: \t $ " + str(guest3_food_2) + "\n Soft Drink: \t\t $ " + 
str(guest1_drink_2) + "\n Water: \t\t $ "+ str(guest2_drink_2) + "\n Soft Drink: \t\t $ " + str(guest3_drink_2) +
"\n Chef Special \t\t $ " + str(table))

table_2_price = float(guest1_food_2 + guest2_food_2 + guest2_food2_2 +
guest3_food_2 + guest1_drink_2 + guest2_drink_2 + guest3_drink_2 + table)
table_2_tax = table_2_price * 0.07
table_2_total = table_2_price + table_2_tax

tip1 = table_2_total * .25
tip2 = table_2_total * .2
tip3 = table_2_total * .15
price_print_2 = print("\t\tPrice: $ " + format(table_2_price, '.2f'))
tax_print_2 = print("\t\tTaxes: $ " + format(table_2_tax,'.2f'))
total_print_2 = print("\t\tTotal: $ " + format(table_2_total, '.2f')) 
print("**Suggested Tip** \nTip 25%: " + format(tip1, '.2f') + 
"\nTip 20%: " + format(tip2, '.2f') + "\nTip 15%: " + format(tip3, '.2f'))


