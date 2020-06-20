"""
Opening up a furniture store called Lovelyseats for Neat Suites on Fleet Street
"""
#description for lovely loveseat
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
# setting price for lovely loveseat
lovely_loveseat_price = 254.00

#description for stylish settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
#setting price for settee
stylish_settee_price = 180.50

#description for luxurious lamp
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
#setting price for luxurious lamp
luxurious_lamp_price = 52.15

#define sales tax to 8.8%
sales_tax = 0.088

#first customer has initiated a purchase
customer_one_total = 0

#list of things purchased
customer_one_itemization = ""

# adding price of Lovely Loveseat and description
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description 
#adding price of Luxurious Lamp and description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#calculate sales tax for first customer

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)





















