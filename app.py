# Signature
# Author: Hicham Essaydi
# Email : hessaydi@gmail.com
# Github: github.com/hessaydi


# Project specifications

"""
Title: Invoice managment application using python

Goal:
Print the global cost of all sales

Inputs:
	Numbers of products: N
	for each product we set:
		Name: name_product
		Price by unit: price_by_unit
		Number of units: units_number
Ouputs:
	Total price: total_price
	detailed graph: printed
"""

product_number = int(input("Enter the number of elements: "))

lst = []
total_price = 0
class Product:
	def __init__(self, product_name, price_by_unit, units_number):
		self.product_name = product_name
		self.price_by_unit = price_by_unit
		self.units_number = units_number
	def __repr__(self):
		return f'<Product Name: {self.product_name} - Price: {self.price_by_unit} - Number: {self.units_number}>'

for i in range(product_number):
	product_name = input(f"Enter product name for {i+1} :")
	price_by_unit = int(input(f"Enter product price by unit for {i+1} :"))
	units_number = int(input(f"Enter units number of product {i+1} :"))

	product = Product(product_name, price_by_unit, units_number)
	lst.append(product)


from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ['Product Name', 'Price By Unit', 'Units Number', 'Total Price of Product']
for item in lst:
	total_price_by_product = item.units_number * item.price_by_unit
	table.append_row([item.product_name,  item.price_by_unit,  item.units_number, total_price_by_product ])
	total_price += total_price_by_product
table.append_row(["Total",None,None,total_price])
print(table)

