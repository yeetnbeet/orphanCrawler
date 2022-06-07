Welcome to the Contender Orphan Page utility
Author: Sam Segal  Email: segalcsam@gmail.com

dependancies:
requests==2.22.0 beautifulsoup4==4.8.1 numpy== current version

Interpreter:
Python 2.7.16

The Program takes a csv of two columns
Column 1        Column 2
URL 1           Description 1
URL 2           Description 2
URL 3           Description 3
...             ...

URl is a /products/PRODUCT_NAME style page for www.contenderbicycles.com

The Program Searches for the (disabled = 'disabled') tag.
This tag is proxy for item out of stock

Data is populated from ahrefs.com export csv (Orphan Pages)
Data is groomed to only include /products pages

-EMPTY OUTPUT DATA CSV FILES BEFORE RUNNING-
console will print number to let you know how far along you are 
*if it encounters an error it will not populate any error
make sure every url exists before running program*

OUTPUT DATA WILL NOT REPRESENT ANYTHING ON A NON-PRODUCT PAGE 
*if using in the far future must check for disable = 'disabled'
tag on product page*

email me if you have questions hopefully I can get back to you!



