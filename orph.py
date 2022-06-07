
from numpy import array
import requests
import csv
from bs4 import BeautifulSoup

# 1. import csv of target urls ~create new csv maybe~
# 2. while loop through targets and find id="AddToCart" and disabled="disabled"
# add to 3D array [[URL,NAME,STATUS],[URL,NAME,STATUS],...]
# 3. Export to new csv or plot the data...
count = 0
empty = []
instockAlert = []
noStock = []

with open('DATA.csv') as csvfile:
    array = csv.reader(csvfile)
    loopableArray = list(array)

for line in loopableArray:
    html_text = requests.get(line[0]).text
    soup = BeautifulSoup(html_text, 'html.parser')
    print(count)
    if soup.find_all("button",{'disabled':'disabled'}) == empty:        
        instockAlert.append([line[1],line[0]])
    else:        
        noStock.append([line[1],line[0]])
    
    count = count+1

print(instockAlert)
print("out stock")
print(noStock)

with open('INSTOCK_OUTPUT.csv', mode = 'w') as INSTOCK:
    instock_writer = csv.writer(INSTOCK,delimiter=',')
    for line in instockAlert:
        instock_writer.writerow(line)

with open('OUTSTOCK_OUTPUT.csv', mode = 'w') as OUTSTOCK:
    outstock_writer = csv.writer(OUTSTOCK,delimiter=',')
    for line in noStock:
        outstock_writer.writerow(line)

print("/nDONE THANK YOU")



#html_text = requests.get('https://contenderbicycles.com/collections/apparel/products/contender-pride-t-shirt').text
#soup = BeautifulSoup(html_text, 'html.parser')
#if soup.find_all("button",{'disabled':'disabled'})== empty:
    #print("instock")
#else:
    #print("out")









 




    
