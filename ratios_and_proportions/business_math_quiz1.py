'''
Let's break down the problem step by step:

a) **Total Cost:**
   The list price is reduced by 7% and then by an additional 4%. 
   The selling price is marked up by 30%. After selling 60% of the shipment, 
   the remaining tables are marked down to a reduced selling price.

   First, calculate the reduced list price after both discounts:
   \[ \text{Reduced List Price} = \$120 - (\$120 \times 0.07) - (\$120 \times 0.04) \]

   Then, calculate the selling price after the 30% markup:
   \[ \text{Selling Price} = \text{Reduced List Price} + (\text{Reduced List Price} \times 0.30) \]

   The total cost is the selling price after the 30% markup.

b) **Regular Selling Price:**
   The regular selling price is the selling price before any markdowns.

c) **Total Sales:**
   The total sales are the sum of the sales from the initial selling price for 60% of the tables 
   and the sales from the reduced selling price for the remaining 40% of the tables.

d) **Sale Price of the Tables:**
   The sale price of the tables is given as $96.99 for the remaining 10 tables.

Let's calculate these values:
'''
# Given values
list_price = 120
discount1 = 0.07
discount2 = 0.04
markup_percentage = 0.30
remaining_markdown_price = 96.99
remaining_tables_percentage = 0.40

# Calculations
reduced_list_price = list_price - (list_price * discount1) - (list_price * discount2)
selling_price = reduced_list_price + (reduced_list_price * markup_percentage)
regular_selling_price = selling_price  # before any markdowns
total_cost = selling_price  # the total cost is the selling price after the 30% markup
total_sales = (0.60 * selling_price) + (remaining_tables_percentage * remaining_markdown_price)

# Output rounded to the nearest cent
print("a) Total Cost:", round(total_cost, 2))
print("b) Regular Selling Price:", round(regular_selling_price, 2))
print("c) Total Sales:", round(total_sales, 2))
print("d) Sale Price of the Tables:", round(remaining_markdown_price, 2))

'''
Please note that the values provided may need to be adjusted based on specific details in the problem statement,
and rounding is done to the nearest cent.

python3 business_math_quiz1.py
'''
