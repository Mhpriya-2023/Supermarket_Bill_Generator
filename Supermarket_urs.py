from datetime import datetime

name=input("Enter your name:")

#list of items
lists='''
Rice     rs 20/kg
Sugar    rs 40/kg
salt     rs 20/kg
oil      rs 120/lit
Paneer   rs 150/kg
Maggie   rs 60/kg
Horlicks rs 88/kg
Brush    rs 20/each
Colgate  rs 38/each
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':20,
'Sugar':40,
'salt':20,
'oil':120,
'Paneer':150,
'Maggie':60,
'Horlicks':88,
'Brush':20,'Colgate':38}

option=int(input("for list of items press 1:"))

if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append(price)
            print(pricelist)
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price) 
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available ")  
            
print(finalamount)      
inp=input("can i bill the items yes or no")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"=","Ours supermarket",25*"=")
        print(28*" ","Urs mart")
        print("Name:",name,30*" ","Date:",datetime.now())
        print(75*"-")
        print("sno",2*" ",'items',4*" ",'quantity',7* " ",'price')
        for i in range(len(pricelist)):
            print(i,1*" ",5*" ",ilist[i],5*" ",qlist[i],7*" ",plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)     
        print("gst amount",50*" ",'Rs',gst)   
        print(75*"-")  
        print(50*" ",'finalAmount:','Rs',finalamount) 
        print(75*"-") 
print(20*" ","<<<<Thanks for visting>>>>") 
print(20*" ",".......Visit Again........")
        
        